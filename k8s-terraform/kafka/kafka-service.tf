# kafka/kafka-service.tf
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