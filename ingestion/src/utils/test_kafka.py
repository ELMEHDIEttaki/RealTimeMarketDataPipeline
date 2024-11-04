import io
import os
import logging
from kafka import KafkaConsumer
import avro.schema
import avro.io
from dotenv import load_dotenv
from function import load_avro_schema, avro_decode

# Setup environment variables
env_file = '.env'
load_dotenv(env_file, override=True)

# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Logger setup
def setup_logger():
    logging.basicConfig(
        filename="logs/consumer.log", 
        level=logging.INFO, 
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("ConsumerLogger")

logger = setup_logger()


def main():
    # Kafka Configuration
    kafka_broker = 'localhost:9092'  # Update as necessary
    kafka_topic = os.getenv('KAFKA_TOPIC', 'market')  # Default to 'market' if not set

    # Avro Schema path
    avro_schema_path = "ingestion/src/schemas/trades.avsc"

    # Load Avro schema
    avro_schema = load_avro_schema(avro_schema_path)

    # Initialize Kafka Consumer
    consumer = KafkaConsumer(
        kafka_topic,
        bootstrap_servers=kafka_broker,
        value_deserializer=lambda x: x  # Receive raw bytes
    )

    logger.info("Listening for messages...")

    try:
        for message in consumer:
            # Log raw Kafka message as bytes
            message_value = message.value
            logger.info(f"Raw message bytes: {message_value}")

            # Decode the Avro-encoded message
            decoded_data = avro_decode(message_value, avro_schema)
            if decoded_data:
                print("Decoded message:", decoded_data)
    except KeyboardInterrupt:
        print("Stopping consumer...")
    finally:
        # Clean up and close the consumer
        consumer.close()

if __name__ == "__main__":
    main()
