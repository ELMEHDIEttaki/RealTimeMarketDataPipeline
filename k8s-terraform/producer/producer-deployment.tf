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
          name  = "twelvedata-producer"
          image = "producer"  # Replace with the actual image name
          port {
            container_port = 8001
          }
          env {
            name  = "BROKER_URL"
            value = "kafka:9092"
          }
          env {
            name  = "API_TOKEN"
            value = "ff11a5aec4414ee9b6db5c6d1053d14f"
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
