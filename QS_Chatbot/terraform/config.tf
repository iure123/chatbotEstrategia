terraform {
  required_version = ">= 1.0.0"

  backend "gcs" {
    bucket = "sz-terraform-444920103265"
    prefix = "terraform/state-qs-chatbot"
  }

  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "~> 4.30.0"
    }
  }
}

provider "google" {
  project = var.GCP_PROJECT
  region  = var.GCP_REGION
}
