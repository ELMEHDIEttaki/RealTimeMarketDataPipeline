import io
#import avro.schema
from avro.io import DatumWriter, BinaryEncoder
import avro.io
import avro.schema
from kafka import KafkaProducer

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

def avro_encode(data, avro_schema):
    writer = avro.io.DatumReader(avro_schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write(data, encoder)
    return bytes_writer.getvalue()

# Automate Message Adaptation
def adapt_message_for_avro(message, expected_fields):
    # Ensure all expected fields are present in the message, filling with None if missing
    for field in expected_fields:
        if field not in message:
            message[field] = None
    return message

    # bytes_writer = io.BytesIO()
    # encoder = BinaryEncoder(bytes_writer)
    # writer = DatumWriter(avro_schema)
    # writer.write(data, encoder)
    # return bytes_writer.getvalue()
