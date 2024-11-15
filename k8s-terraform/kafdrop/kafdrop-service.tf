# kafdrop/kafdrop-service.tf
# resource "kubernetes_service" "kafdrop" {
#   metadata {
#     name      = "kafdrop-service"
#     namespace = var.namespace 
#   }
#   spec {
#     selector = {
#       app = "kafdrop"
#     }

#     type = "LoadBalancer"

#     port {
#       port        = 9000
#       target_port = 9000
#     }
#   }
# }


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
