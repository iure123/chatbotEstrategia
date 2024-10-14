resource "google_storage_bucket" "storage-cloud-qs-chatbot" {
  name          = "storage-${var.APP_NAME}-${var.ENVIRONMENT_SUFIX}"
  location      = var.GCP_REGION
  force_destroy = true
  project       = var.GCP_PROJECT
  storage_class = "STANDARD"

  uniform_bucket_level_access = true
}