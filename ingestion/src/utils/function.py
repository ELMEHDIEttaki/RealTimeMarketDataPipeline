#import io
#import avro.schema
# from avro.io import DatumWriter, BinaryEncoder
# import avro.io
# import avro.schema
import io
import avro.schema
import avro.io
import json
from kafka import KafkaProducer
import logging
import os


# Create logs directory if it doesn't exist
if not os.path.exists("logs"):
    os.makedirs("logs")

# Logger setup
def setup_logger():
    logging.basicConfig(
        filename="logs/avro.log", 
        level=logging.INFO, 
        format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
    )
    return logging.getLogger("AppLogger")

logger = setup_logger()


def load_producer(kafka_server):
    """Initialize Kafka producer."""
    return KafkaProducer(bootstrap_servers=kafka_server)

def load_avro_schema(schema_path):
    """Load and parse the Avro schema from file."""
    # with open(schema_path, 'r') as schema_file:
    #     return avro.schema.parse(schema_file.read())
    return avro.schema.parse(open(schema_path).read())

# def avro_encode(data, schema):
#     """Encode a data dictionary into Avro format."""
#     writer = avro.io.DatumWriter(schema)
#     bytes_writer = io.BytesIO()
#     encoder = avro.io.BinaryEncoder(bytes_writer)
#     writer.write(data, encoder)
#     return bytes_writer.getvalue()

# Automate Message Adaptation
def adapt_message_for_avro(message, expected_fields):
    # Ensure all expected fields are present in the message, filling with None if missing
    for field in expected_fields:
        if field not in message:
            message[field] = None
    return message


# def avro_encode(data, avro_schema):
#     writer = avro.io.DatumWriter(avro_schema)
#     bytes_writer = io.BytesIO()
#     encoder = avro.io.BinaryEncoder(bytes_writer)
#     writer.write(data, encoder)
#     return bytes_writer.getvalue()

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
    
    #logger.info(f"AVRO_BYTES: {avro_bytes}")
    
    # # Now we need to decode it back to a dictionary
    # bytes_reader = io.BytesIO(avro_bytes)
    # logger.info(f"BYTES_READER: {bytes_reader}")
    # decoder = avro.io.BinaryDecoder(bytes_reader)
    # logger.info(f"AVRO_DECODER_BYTES: {decoder}")
    # reader = avro.io.DatumReader(avro_schema)
    # logger.info(f"AVRO_BYTES_READER: {reader}")
    
    # # Read and return the data as a dictionary
    # decoded_data = reader.read(decoder)
    # logger.info(f"decoded_data: {decoded_data}")
    
    return avro_bytes

    # bytes_writer = io.BytesIO()
    # encoder = BinaryEncoder(bytes_writer)
    # writer = DatumWriter(avro_schema)
    # writer.write(data, encoder)
    # return bytes_writer.getvalue()
