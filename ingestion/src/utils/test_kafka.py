from kafka import KafkaConsumer
#from fastavro.schema import load_schema
from function import load_avro_schema
from fastavro import schemaless_reader
import io
from dotenv import load_dotenv
import os

# Setup environment variables
env_file = '.env'
load_dotenv(env_file, override=True)

# Kafka Configuration
kafka_broker = 'localhost:9092'  # Update with your Kafka broker
kafka_topic = os.getenv('KAFKA_TOPIC') # Update with your Kafka topic
print(kafka_topic)
# Avro Schema (load the Avro schema from a .avsc file)
avro_schema_path = 'ingestion/src/schemas/trades.avsc'
avro_schema = load_avro_schema(avro_schema_path)
print(avro_schema)
# Initialize Kafka Consumer
# consumer_config = {
#     'bootstrap_servers': kafka_broker,

    
#         }
# #consumer = KafkaConsumer(**consumer_config)
# consumer  = KafkaConsumer(*kafka_topic, **consumer_config)

# Initialize Kafka Consumer with the correct configuration keys
consumer = KafkaConsumer(
    kafka_topic,
    bootstrap_servers=kafka_broker,
    value_deserializer=lambda x: x  # Do not decode; we'll use Avro decoding
)
print(consumer.poll())
# Subscribe to the kafka topic 
#print(consumer.subscribe(kafka_topic))

#for now we can include all messages from market kafka topic

# try:
#     print("Listening for messages...")
#     while True:
#         # Poll for messages
#         msg_pack = consumer.poll(timeout_ms=1000)  # Poll for messages with 1-second timeout
#         print(msg_pack)
#         for tp, messages in msg_pack.items():
#             for msg in messages:
#                 # Raw message content
#                 message_value = msg.value
#                 print(f"Raw message: {message_value}")

#                 # Decode the Avro-encoded message
#                 try:
#                     decoded_data = schemaless_reader(io.BytesIO(message_value), avro_schema)
#                     print("Decoded message:", decoded_data)
#                 except Exception as e:
#                     print(f"Failed to decode message: {e}")

# Listening for messages
print("Listening for messages...")

try:
    while True:
         # Poll for messages
         msg_pack = consumer.poll(timeout_ms=1000)  # Poll for messages with 1-second timeout
         print(msg_pack)
         for tp, messages in msg_pack.items():
            for msg in consumer:
                print(msg)
                # Log raw Kafka message as bytes
                message_value = msg.value
                print(f"Raw message bytes: {message_value}")
                # Decode the Avro-encoded message
                try:
                    decoded_data = schemaless_reader(io.BytesIO(message_value), avro_schema)
                    print("Decoded message:", decoded_data)
                except Exception as e:
                    print(f"Failed to decode message: {e}")

except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    # Clean up and close the consumer
    consumer.close()