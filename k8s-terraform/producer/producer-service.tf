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
