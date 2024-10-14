resource "google_artifact_registry_repository" "qs-chatbot" {
  project       = var.GCP_PROJECT
  location      = var.GCP_REGION
  repository_id = "qs-chatbot"
  description   = "Repositorio imagens Docker - qs-chatbot"
  format        = "DOCKER"
}