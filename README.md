# **MarketDataStreamPipeline**

## **Overview**
**MarketDataStreamPipeline** is a scalable, real-time data pipeline designed to process and visualize market data from the TwelveData's websocket API. This architecture integrates multiple powerful components:
- **Apache Kafka** for reliable message brokering
- **Apache Spark** for data processing
- **Cassandra** for distributed storage
- **Grafana** for visualization
- **Kubernetes** for container orchestration
- **Terraform** for infrastructure provisioning

This repository will provides all the code, configuration, and instructions needed to deploy and operate the pipeline.

---

## **Architecture**
![Architecture](Architecture.png)
### **Data Flow**
1. **Ingestion**: The pipeline ingests real-time data from the TwelveData WebSocket API using a custom Python producer.
2. **Message Broker**: Kafka acts as the message broker, handling data distribution between ingestion and processing stages.
3. **Stream Processing**: Apache Spark processes the streaming data to perform transformations and analytical computations.
4. **Serving Database**: Processed data is stored in a Cassandra database, allowing for efficient querying and storage at scale.
5. **Visualization**: Grafana is configured to visualize the data stored in Cassandra, providing real-time insights and dashboards.
6. **Infrastructure Management**: The entire pipeline runs on Kubernetes, with Terraform scripts for automated provisioning and configuration.

---

## **Project Structure**
The project is organized into the following directories:

```
MarketDataStreamPipeline/
│
├── ingestion/
│   ├── twelve_data_producer.py      # Python producer to ingest data from TwelveData API
│   ├── config.json                  # Configuration file for producer settings
│   └── Dockerfile                   # Dockerfile to containerize the producer
│
├── message-broker/
│   ├── kafka/
│   │   ├── docker-compose.yml       # Docker Compose file for Kafka and Zookeeper
│   │   └── config/                  # Kafka configuration files
│   └── kafdrop/                     # Kafdrop UI for Kafka monitoring
│
├── stream-processing/
│   ├── stream_processor.py    # Spark code for processing Kafka streams
│   └── Dockerfile                   # Dockerfile for Spark container
│
├── database/
│   ├── cassandra-setup.cql          # Script to initialize Cassandra keyspaces and tables
│   └── Dockerfile                   # Dockerfile for Cassandra container
│
├── visualization/
│   ├── grafana/
│   │   └── dashboard.js             # Grafana dashboard configuration
│   └── Dockerfile                   # Dockerfile for Grafana
│
├── infrastructure/
│   ├── terraform/                   # Terraform scripts for infrastructure setup
│   └── kubernetes/                  # Kubernetes deployment files
│
└── README.md                        # Project documentation
```

---