import time
from twelvedata import TDClient  # Replace with the actual TwelveData client library if different
from src.utils.function import load_producer, load_avro_schema, avro_encode
import os
from dotenv import load_dotenv
import logging

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Set up the logger
logging.basicConfig(filename="logs/app.log", 
                    level=logging.INFO, 
                    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s")
# Get the logger
logger = logging.getLogger("AppLogger")

env_file = '.env'
load_dotenv(env_file, override=True)


class TwelveDataPipeline:
    def __init__(self, api_token, kafka_server, schema_path):
        self.api_token = api_token
        self.kafka_server = kafka_server
        self.schema_path = schema_path
        self.twelvedata_client = self._load_client()
        self.kafka_producer = load_producer(kafka_server)
        self.avro_schema = load_avro_schema(schema_path)

    # Initialize connection to TwelveData API
    def _load_client(self):
        """Initialize the TwelveData client."""
        return TDClient(apikey=self.api_token)
    
    def sub(self, stat):
        ws = self.twelvedata_client.websocket(tickers=tickers, on_event=on_event)
        if stat == 'connect':
            ws.subscribe(tickers)
            ws.connect()
            ws.heartbeat()
        elif stat == 'disconnect':
            ws.disconnect()


    def lookup_ticker(self, ticker):
        """Look up ticker in TwelveData."""
        return self.twelvedata_client.symbol_search(symbol=ticker).as_json()


    def ticker_validator(self, ticker):
        """Validate if a ticker exists in TwelveData."""
        for stock in self.lookup_ticker(ticker):
            if stock['symbol'] == ticker:
                return True
        return False

    def send_to_kafka(self, topic, data):
        """Send encoded data to Kafka."""
        encoded_data = avro_encode(data, self.avro_schema)
        self.kafka_producer.send(topic, encoded_data)
        self.kafka_producer.flush()
        print(f"Sent data to Kafka topic '{topic}'")


# Example usage
if __name__ == "__main__":
    # Set your parameters here
    API_TOKEN = os.getenv('API_KEY')
    KAFKA_SERVER = "localhost:9092"
    KAFKA_TOPIC = "market"
    SCHEMA_PATH = "ingestion/src/schemas/trades.avsc" 


    tickers = ['BTC/USD', 'ETH/BTC', 'AAPL']
    historical_messages = []
    
    def on_event(e):
        #print(e)
        historical_messages.append(e)
    
    # Initialize pipeline
    pipeline = TwelveDataPipeline(api_token=API_TOKEN, kafka_server=KAFKA_SERVER, schema_path=SCHEMA_PATH)

    # Validate ticker
    #ticker = "AAPL"

    for ticker in tickers: 
        if pipeline.ticker_validator(ticker):
            logger.info(f"Ticker '{ticker}' is valid.")
        else:
            logger.info(f"Ticker '{ticker}' is not valid.")

    try:
        while True:
            pipeline.sub(stat='connect')
            for message in historical_messages:
                logger.info(f"Display Message without select event: {message}")
                if message.get('event') == "price":
                    logger.info(f"Display Message: {message}")
                    pipeline.send_to_kafka(topic=KAFKA_TOPIC, value=message)
            logger.info(f"Messages published to Kafka topic: {KAFKA_TOPIC}")
            time.sleep(10)
    except KeyboardInterrupt:
        print("Interrupted by me :) !")
    finally:
        pipeline.sub(stat='disconnect')
















            
        # Send sample data to Kafka
        #sample_data = {
        #    "ticker": "AAPL",
        #    "price": 150.0,
        #    "timestamp": "2023-01-01T12:00:00Z"
        #}
        #pipeline.send_to_kafka(topic="market_data", data=sample_data)