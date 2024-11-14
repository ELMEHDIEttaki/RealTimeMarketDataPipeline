# zookeeper/zookeeper-deployment.tf
resource "kubernetes_deployment" "zookeeper" {
  metadata {
    name = "zookeeper"
    labels = {
      app = "zookeeper"
    }
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "zookeeper"
      }
    }
    template {
      metadata {
        labels = {
          app = "zookeeper"
        }
      }
      spec {
        container {
          name  = "zookeeper"
          image = "docker.io/bitnami/zookeeper:3.9"
          port {
            container_port = 2181
          }
          env {
            name  = "ALLOW_ANONYMOUS_LOGIN"
            value = "yes"
          }
          env {
            name  = "ZOOKEEPER_CLIENT_PORT"
            value = "2181"
          }
        }
      }
    }
  }
}