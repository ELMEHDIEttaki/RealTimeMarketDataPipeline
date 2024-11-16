# kafdrop/outputs.tf
output "service_url" {
  value = try(
    kubernetes_service.kafdrop.status[0].load_balancer[0].ingress[0].hostname,
    ""
  )
  description = "The URL of the Kafdrop service"
}