resource "google_cloud_run_service" "qs-chatbot" {
  name     = var.APP_NAME
  location = var.GCP_REGION
  

  template {
    spec {
      containers {
        image = "gcr.io/sz-academia-digital-feat/qs_chatbot@sha256:ca352b38e972a93f964cf07a06f753e76481e32562c56abff50a070785c1e700"
        resources {
          limits = {
            memory = "1024Mi"
          }
        }
        env {
          name  = "APP_URL"
          value = "https://${var.APP_NAME}-${var.URL_SUFIX}"
        }
        env {
          name  = "PROJECT_ID"
          value = var.GCP_PROJECT
        }
        env {
          name  = "SECRET_ID"
          value = var.SECRET_ID
        }
      }
      service_account_name = data.terraform_remote_state.main_project_state_data.outputs.application_ai_service_account
    }
    metadata {
      annotations = {
        "autoscaling.knative.dev/maxScale" = "10"
      }
    }
  }

  traffic {
    percent         = 100
    latest_revision = true
  }

  depends_on = [
    data.terraform_remote_state.main_project_state_data
  ]
}

data "google_iam_policy" "noauth" {
  binding {
    role = "roles/run.invoker"
    members = [
      "allUsers",
    ]
  }
}

resource "google_cloud_run_service_iam_policy" "noauth" {
  location    = google_cloud_run_service.qs-chatbot.location
  project     = google_cloud_run_service.qs-chatbot.project
  service     = google_cloud_run_service.qs-chatbot.name

  policy_data = data.google_iam_policy.noauth.policy_data
}
