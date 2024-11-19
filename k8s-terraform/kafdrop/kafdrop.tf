# kafdrop/kafdrop-deployment.tf

variable "kafdrop_image" {
  description = "Kafdrop Image for kafka monitoring"
  type        = string
  #default     = "docker.io/obsidiandynamics/kafdrop:latest"
  
}

resource "kubernetes_deployment" "kafdrop" {
  metadata {
    name = "kafdrop"
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
          image = "var.kafdrop_image"
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


resource "kubernetes_service" "kafdrop" {
  metadata {
    name      = "kafdrop-service"
  }

  spec {
    selector = {
      app = "kafdrop"
    }

    type = "LoadBalancer"

    port {
      port        = 9000
      target_port = 9000
    }
  }
}
