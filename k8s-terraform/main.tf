# main.tf

# Configure the Kubernetes provider
provider "kubernetes" {
  config_path = var.kubeconfig_path
}


# Zookeeper Deployment
module "zookeeper" {
  source = "./zookeeper"
}

# Kafka Deployment
module "kafka" {
  source = "./kafka"
}

# Kafdrop Deployment
module "kafdrop" {
  source = "./kafdrop"
  #namespace = var.namespace
}

# Producer Deployment
module "producer" {
  source = "./producer"
}

# Define the Kubernetes namespace
resource "kubernetes_namespace" "ecosystem" {
  metadata {
    name = var.namespace
  }
}
