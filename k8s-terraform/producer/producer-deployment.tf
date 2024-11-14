# producer/producer-deployment.tf
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
          name  = "producer"
          image = "your-docker-image"  # Replace with the actual image name
          port {
            container_port = 8001
          }
          env {
            name  = "BROKER_URL"
            value = "kafka:9092"
          }
          env {
            name  = "API_TOKEN"
            value = "your_api_token"
          }
          env {
            name  = "KAFKA_TOPIC"
            value = "market"
          }
        }
      }
    }
  }
}
