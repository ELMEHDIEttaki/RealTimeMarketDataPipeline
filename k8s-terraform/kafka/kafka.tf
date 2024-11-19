# kafka/kafka-deployment
variable "kafka_image" {
  description = "Docker image for Kafka"
  type        = string
  default     = "docker.io/bitnami/kafka:latest"
}

resource "kubernetes_deployment" "kafka" {
  metadata {
    name = "kafka"
    labels = {
      app = "kafka"
    }
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "kafka"
      }
    }
    template {
      metadata {
        labels = {
          app = "kafka"
        }
      }
      spec {
        container {
          name  = "kafka"
          image = var.kafka_image
          port {
            container_port = 9092
          }
          env {
            name  = "KAFKA_BROKER_ID"
            value = "1"
          }
          env {
            name  = "KAFKA_ZOOKEEPER_CONNECT"
            value = "zookeeper:2181"
          }
          # Other necessary environment variables
          env {
            name  = "KAFKA_LISTENERS"
            value = "INTERNAL://0.0.0.0:29092,EXTERNAL://0.0.0.0:9092"
          }
          env {
            name  = "KAFKA_ADVERTISED_LISTENERS"
            value = "INTERNAL://kafka:29092,EXTERNAL://localhost:9092"
          }
          env {
            name  = "KAFKA_LISTENER_SECURITY_PROTOCOL_MAP"
            value = "INTERNAL:PLAINTEXT,EXTERNAL:PLAINTEXT"
          }
          env {
            name  = "KAFKA_INTER_BROKER_LISTENER_NAME"
            value = "INTERNAL"
          }
          env {
            name  = "KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR"
            value = "1"
          }
          env {
            name  = "KAFKA_TRANSACTION_STATE_LOG_MIN_ISR"
            value = "1"
          }
          env {
            name  = "KAFKA_TRANSACTION_STATE_LOG_REPLICATION_FACTOR"
            value = "1"
          }
        }
      }
    }
  }
}

# kafka/kafka-service
resource "kubernetes_service" "kafka" {
  metadata {
    name = "kafka"
  }
  spec {
    selector = {
      app = "kafka"
    }
    port {
      port        = 9092
      target_port = 9092
    }
  }
}