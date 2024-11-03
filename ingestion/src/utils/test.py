import avro.io


with open('ingestion/src/schemas/trades.avsc', 'r') as schema_file:
    print(avro.schema.parse(schema_file.read()))