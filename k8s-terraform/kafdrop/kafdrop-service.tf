# kafdrop/kafdrop-service.tf
resource "kubernetes_service" "kafdrop" {
  metadata {
    name = "kafdrop"
  }
  spec {
    selector = {
      app = "kafdrop"
    }
    port {
      port        = 9000
      target_port = 9000
    }
  }
}