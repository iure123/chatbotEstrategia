## Resources Variables ###

variable "GCP_PROJECT" {
  type        = string
  description = "GCP project id"
}

variable "GCP_REGION" {
  type        = string
  description = "GCP region"
}

variable "ENVIRONMENT_SUFIX" {
  type        = string
  description = "Environment Sufix"
}

variable "TERRAFORM_BUCKET" {
  type        = string
  description = "Bucket Terraform"
}

variable "DOCKER_IMAGE" {
  description = "Docker image for the application"
  default     = "southamerica-east1-docker.pkg.dev/sz-academia-digital-feat/qs-chatbot/qs-chatbot:latest"
}

variable "URL_SUFIX" {
  type        = string
  description = "Sufixo de url Cloud Run"
}

variable "SECRET_ID" {
  type        = string
  description = "Id Secret Manager"
}

variable "APP_NAME" {
  type        = string
  description = "Nome da Aplicaçao"
}