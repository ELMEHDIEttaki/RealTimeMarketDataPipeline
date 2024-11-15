# kafdrop/kafdrop-deployment.tf
resource "kubernetes_deployment" "kafdrop" {
  metadata {
    name = "kafdrop"
    namespace = variables.namespace
    labels = {
      app = "kafdrop"
    }
  }
  spec {
    replicas = 1
    selector {
      match_labels = {
        app = "kafdrop"
      }
    }
    template {
      metadata {
        labels = {
          app = "kafdrop"
        }
      }
      spec {
        container {
          name  = "kafdrop"
          image = "docker.io/obsidiandynamics/kafdrop:latest"
          port {
            container_port = 9000
          }
          env {
            name  = "KAFKA_BROKERCONNECT"
            value = "kafka:9092"
          }
        }
      }
    }
  }
}