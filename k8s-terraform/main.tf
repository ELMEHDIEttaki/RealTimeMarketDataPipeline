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


# Define the Kubernetes namespace
resource "kubernetes_namespace" "ecosystem" {
  metadata {
    name = var.namespace
  }
}

# Zookeeper Deployment
#module "zookeeper" {
#  source = "./zookeeper"
#  zookeeper_image = var.zookeeper_image
#}

# Kafka Deployment
#module "kafka" {
#  source = "./kafka"
#  kafka_image = var.kafka_image
#}

# Kafdrop Deployment
#module "kafdrop" {
#  source = "./kafdrop"
#  kafdrop_image = var.kafdrop_image
#}

# Producer Deployment
#module "producer" {
#  source = "./producer"
#}

