import io
import avro.schema
import avro.io
from kafka import KafkaProducer

def load_producer(kafka_server):
    """Initialize Kafka producer."""
    return KafkaProducer(bootstrap_servers=kafka_server)

def load_avro_schema(schema_path):
    """Load and parse the Avro schema from file."""
    with open(schema_path, 'r') as schema_file:
        return avro.schema.parse(schema_file.read())

def avro_encode(data, schema):
    """Encode a data dictionary into Avro format."""
    writer = avro.io.DatumWriter(schema)
    bytes_writer = io.BytesIO()
    encoder = avro.io.BinaryEncoder(bytes_writer)
    writer.write(data, encoder)
    return bytes_writer.getvalue()
