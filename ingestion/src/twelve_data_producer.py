import time
import os
import logging
from twelvedata import TDClient  # Replace with the actual TwelveData client library if different
from dotenv import load_dotenv
from utils.function import (load_producer, load_avro_schema, 
                            avro_encode, adapt_message_for_avro)

# Logger setup
def setup_logger():
    logging.basicConfig(
        filename="logs/app.log", 
        level=logging.INFO, 
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("AppLogger")

logger = setup_logger()

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Setup environment variables
env_file = '.env'
load_dotenv(env_file, override=True)


class TwelveDataPipeline:
    def __init__(self, api_token, kafka_server, schema_path):
        self.api_token = api_token
        self.kafka_server = kafka_server
        self.schema_path = schema_path
        self.twelvedata_client = self._initialize_client()
        self.kafka_producer = load_producer(kafka_server)
        self.avro_schema = load_avro_schema(schema_path)
        self.websocket = None  # Initialized during subscription

    def _initialize_client(self):
        """Initialize the TwelveData client."""
        return TDClient(apikey=self.api_token)

    def manage_subscription(self, tickers, action):
        """Manage websocket connection to TwelveData."""
        if not self.websocket:
            self.websocket = self.twelvedata_client.websocket(
                tickers=tickers, on_event=self.on_event
            )
        if action == 'connect':
            self.websocket.subscribe(tickers)
            self.websocket.connect()
            self.websocket.heartbeat()
        elif action == 'disconnect' and self.websocket:
            self.websocket.disconnect()

    def lookup_ticker(self, ticker):
        """Look up ticker symbol on TwelveData."""
        return self.twelvedata_client.symbol_search(symbol=ticker).as_json()

    def validate_ticker(self, ticker):
        """Check if ticker exists in TwelveData."""
        return any(stock['symbol'] == ticker for stock in self.lookup_ticker(ticker))

    def send_to_kafka(self, topic, data):
        """Encode and send data to Kafka."""
        try:
            encoded_data = avro_encode(data, self.avro_schema)
            logger.info(f"Display encoded data content: {encoded_data}")
            self.kafka_producer.send(topic, encoded_data)
            self.kafka_producer.flush()
            logger.info(f"Sent data to Kafka topic '{topic}'")
        except Exception as e:
            logger.error(f"Failed to send data to kafka: {e}")

    @staticmethod
    def on_event(event):
        """Event handler for TwelveData websocket."""
        historical_messages.append(event)  # Store events for later processing

    # Helper functions for the main execution flow
    def validate_tickers(self, tickers):
        """Validate tickers and log their validity."""
        for ticker in tickers:
            if self.validate_ticker(ticker):
                logger.info(f"Ticker '{ticker}' is valid.")
            else:
                logger.info(f"Ticker '{ticker}' is not valid.")

    # sent messages to kafka broker
    def publish_messages_to_kafka(self, topic):
        """Publish messages to Kafka topic."""
        expected_fields = [
                "event", "symbol", "currency_base", "currency_quote",
                "exchange", "type", "timestamp", "price", "bid", "ask", "day_volume"
            ]
        for message in historical_messages:
            logger.info(f"message befor select price event: {message }")
            if message.get('event') == "price":
                adapted_message = adapt_message_for_avro(message, expected_fields)
                logger.info(f"selected price event with adaptation approach: {adapted_message}")
                
                # Encode and publish to Kafka
                logger.info(f"Publishing... message: {adapted_message}")
                self.send_to_kafka(topic=topic, data=message)
                logger.info(f"sent message to kafka: {adapted_message}")
        logger.info(f"Messages published to Kafka topic: {topic}")

# Main execution
if __name__ == "__main__":
    # Load configurations from environment
    API_TOKEN = os.getenv('API_TOKEN')
    logger.info(f"API-TOKEN : {API_TOKEN}")
    KAFKA_SERVER = os.getenv('BROKER_URL')
    logger.info(f"KAFKA_SERVER : {KAFKA_SERVER}")
    SCHEMA_PATH = "ingestion/src/schemas/trades.avsc"
    KAFKA_TOPIC = os.getenv('KAFKA_TOPIC')
    logger.info(f"KAFKA TOPIC NAME : {KAFKA_TOPIC}")

    # Set tickers and initialize message storage
    tickers = ['BTC/USD', 'ETH/BTC', 'AAPL']
    historical_messages = []

    # Initialize TwelveData pipeline
    pipeline = TwelveDataPipeline(
        api_token=API_TOKEN, 
        kafka_server=KAFKA_SERVER, 
        schema_path=SCHEMA_PATH
    )
    # Validate tickers
    pipeline.validate_tickers(tickers)

    try:
        while True:
            pipeline.manage_subscription(tickers=tickers, action='connect')
            pipeline.publish_messages_to_kafka(topic=KAFKA_TOPIC)
            time.sleep(10)
    except KeyboardInterrupt:
        print("Process interrupted by user.")
    finally:
        pipeline.manage_subscription(tickers=tickers, action='disconnect')
