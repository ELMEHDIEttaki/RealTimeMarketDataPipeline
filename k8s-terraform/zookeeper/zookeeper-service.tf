# zookeeper/zookeeper-service.tf
resource "kubernetes_service" "zookeeper" {
  metadata {
    name = "zookeeper"
  }
  spec {
    selector = {
      app = "zookeeper"
    }
    port {
      port        = 2181
      target_port = 2181
    }
  }
}