FROM python:3.10.12

# Set the working directory
WORKDIR /app

# Copy the entire project directory into the container

COPY . .

RUN pip install --upgrade pip

RUN pip install -r ingestion/requirements.txt

CMD ["python3","ingestion/src/twelve_data_producer.py"]
