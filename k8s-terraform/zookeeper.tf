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
          image = var.zookeeper_image
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