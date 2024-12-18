# variables.tf

# Path to the kubeconfig file to connect to the Kubernetes cluster
variable "kubeconfig_path" {
  description = "Path to kubeconfig file"
  type        = string
  default     = "~/.kube/config"
}

# Kubernetes namespace for the deployments
variable "namespace" {
  description = "Namespace for ecosystem deployments"
  type        = string
  default     = "ecosystem"
}

# Kafka and Zookeeper Image Versions
variable "kafka_image" {
  description = "Docker image for Kafka"
  type        = string
  default     = "docker.io/bitnami/kafka:latest"
}

variable "zookeeper_image" {
  description = "Docker image for Zookeeper"
  type        = string
  default     = "docker.io/bitnami/zookeeper:3.9"
}

variable "kafdrop_image" {
  description = "Kafdrop Image for kafka monitoring"
  type        = string
  default     = "docker.io/obsidiandynamics/kafdrop:latest"  
}

# Producer API Token
#variable "api_token" {
#  description = "API token for producer"
#  type        = string
#  default     = "ff11a5aec4414ee9b6db5c6d1053d14f"
#}

# Kafka Topic
#variable "kafka_topic" {
#  description = "Kafka topic for producer"
#  type        = string
#  default     = "market"
#}

# Output the Kafdrop Service URL
# output "kafdrop_service_url" {
#   description = "URL to access the Kafdrop service for monitoring Kafka topics"
#   value       = module.kafdrop.status.load_balancer[0].ingress[0].hostname
#   depends_on  = [kubernetes_service.kafdrop]
# }

# output "kafdrop_service_url" {
#   description = "URL to access the Kafdrop service for monitoring Kafka topics"
#   value       = module.kafdrop.kafdrop_service.kafdrop.status.load_balancer[0].ingress[0].hostname
#   depends_on  = [module.kafdrop.kubernetes_service.kafdrop]
# }

# variables.tf (or where your outputs are defined)
# output "kafdrop_service_url" {
#   value       = module.kafdrop.service_url
#   depends_on  = [module.kafdrop]
# }
