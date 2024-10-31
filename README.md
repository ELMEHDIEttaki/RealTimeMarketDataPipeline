# RealTimeMarketDataPipeline
RealTimeMarketDataPipeline is a robust, end-to-end real-time data pipeline designed for processing and visualizing market data from TwelveData’s WebSocket API.


![Architecture](Architecture.png)
This architecture leverages Apache Kafka for message brokering, Apache Spark for real-time stream processing, Cassandra for scalable data storage, and Grafana for visualization.

The project is containerized using Docker and orchestrated on Kubernetes, making it scalable, flexible, and suitable for cloud deployment. Infrastructure provisioning and management are automated with Terraform, simplifying deployment and scaling across various environments.

## Features
**Real-Time Data Ingestion**: Capture live market data from TwelveData’s WebSocket API and publish it to Kafka topics.
**Stream Processing with Spark**: Perform transformations and analysis on streaming data using Apache Spark.
**Scalable Storage with Cassandra**: Store processed data in Cassandra for efficient querying and historical analysis.
**Visualization with Grafana**: Monitor and visualize market trends in real time.
**Infrastructure as Code (IaC)**: Easily deploy and manage the pipeline using Kubernetes and Terraform.

