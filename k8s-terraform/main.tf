# main.tf
terraform {
  required_providers {
    kubernetes = {
      source = "hashicorp/kubernetes"
      version = "2.11.0"
    }
    helm = {
      source = "hashicorp/helm"
      version = "2.9.0"
    }
    kubectl = {
      source = "gavinbunney/kubectl"
      version = "1.14.0"
    }
  }
}

provider "kubernetes" {
  config_path    = pathexpand(var.kubeconfig_path)
  config_context = "minikube"
}

provider "helm" {
  kubernetes {
    config_path = pathexpand(var.kubeconfig_path)
  }
}

#this one is used to deploy SparkApplication properly
provider "kubectl" {}



# Configure the Kubernetes provider
# provider "kubernetes" {
#   config_path = var.kubeconfig_path
# }



# Define the Kubernetes namespace
resource "kubernetes_namespace" "ecosystem" {
  metadata {
    name = var.namespace
  }
}

# Zookeeper Deployment
module "zookeeper" {
  source = "k8s-terraform/zookeeper.tf"
}

# Kafka Deployment
module "kafka" {
  source = "k8s-terraform/kafka.tf"
}

# Kafdrop Deployment
module "kafdrop" {
  source = "k8s-terraform/kafdrop.tf"
  #namespace = var.namespace
}

# Producer Deployment
module "producer" {
  source = "k8s-terraform/producer.tf"
}

