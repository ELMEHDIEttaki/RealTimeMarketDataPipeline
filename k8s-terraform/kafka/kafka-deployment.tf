# kafka/kafka-deployment.tf
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
          image = "docker.io/bitnami/kafka:latest"
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
        }
      }
    }
  }
}