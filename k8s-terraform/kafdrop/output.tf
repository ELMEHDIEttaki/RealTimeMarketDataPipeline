output "service_url" {
  value = kubernetes_service.kafdrop.status.load_balancer[0].ingress[0].hostname
}