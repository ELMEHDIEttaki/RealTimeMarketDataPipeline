# producer/producer-deployment.tf

variable "api_token" {
  description = "API token for producer"
  type        = string
  default     = "ff11a5aec4414ee9b6db5c6d1053d14f"
}

# Kafka Topic
variable "kafka_topic" {
  description = "Kafka topic for producer"
  type        = string
  default     = "market"
}

resource "kubernetes_deployment" "producer" {
  metadata {
    name = "twelvedata-producer"
    labels = {
      app = "producer"
    }
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "producer"
      }
    }
    template {
      metadata {
        labels = {
          app = "producer"
        }
      }
      spec {
        container {
          name  = "twelvedata-producer"
          image = "producer:latest"  # Replace with the actual image name
          port {
            container_port = 8001
          }
          env {
            name  = "BROKER_URL"
            value = "kafka:9092"
          }
          env {
            name  = "API_TOKEN"
            value = var.api_token
          }
          env {
            name  = "KAFKA_TOPIC"
            value = var.kafka_topic
          }
        }
      }
    }
  }
}

# producer/producer-service.tf

resource "kubernetes_service" "producer" {
  metadata {
    name = "producer"
    labels = {
      app = "producer"
    }
  }
  spec {
    selector = {
      app = "producer"
    }
    port {
      # Service port that clients will connect to
      port        = 8001
      target_port = 8001
    }
}
}
