FROM python:3.10.12

# Set the working directory
WORKDIR /ingestion

# Copy the entire project directory into the container

COPY . .

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python3","twelve_data_producer.py"]
