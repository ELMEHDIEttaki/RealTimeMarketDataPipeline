import io
import avro.schema
import avro.io
from kafka import KafkaProducer
import logging
import os


# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Logger setup
def setup_logger():
    logging.basicConfig(
        filename="logs/app.log", 
        level=logging.INFO, 
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("AppLogger")

logger = setup_logger()


def load_producer(kafka_server):
    """Initialize Kafka producer."""
    return KafkaProducer(bootstrap_servers=kafka_server)

def load_avro_schema(schema_path):
    """Load and parse the Avro schema from a file."""
    try:
        with open(schema_path, 'r') as schema_file:
            schema = avro.schema.parse(schema_file.read())
        return schema
    except Exception as e:
        logger.error(f"Failed to load Avro schema: {e}")
        raise

# Automate Message Adaptation
def adapt_message_for_avro(message, expected_fields):
    # Ensure all expected fields are present in the message, filling with None if missing
    for field in expected_fields:
        if field not in message:
            message[field] = None
    return message

# Encode data supported with avro schema
def avro_encode(data, avro_schema):
    # Create a DatumWriter with the provided Avro schema
    writer = avro.io.DatumWriter(avro_schema)
    
    # Create a BytesIO buffer to hold the serialized data
    bytes_writer = io.BytesIO()
    
    # Create a BinaryEncoder that writes to the buffer
    encoder = avro.io.BinaryEncoder(bytes_writer)
    
    # Write the data using the DatumWriter and BinaryEncoder
    writer.write(data, encoder)
    
    # Get the raw bytes
    avro_bytes = bytes_writer.getvalue()
    
    return avro_bytes

def avro_decode(avro_bytes, avro_schema):
    """Decode Avro bytes into a dictionary."""
    try:
        bytes_reader = io.BytesIO(avro_bytes)
        decoder = avro.io.BinaryDecoder(bytes_reader)
        reader = avro.io.DatumReader(avro_schema)
        decoded_data = reader.read(decoder)
        logger.info(f"Decoded data: {decoded_data}")
        return decoded_data
    except Exception as e:
        logger.error(f"Failed to decode message: {e}")
        return None

