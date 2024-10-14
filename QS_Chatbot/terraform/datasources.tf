# Datasource utilizado para adquirir informações do state que contem
# recursos criados pelo projeto principal, tetrys-interface
data "terraform_remote_state" "main_project_state_data" {
  backend = "gcs"
  config = {
    bucket  = var.TERRAFORM_BUCKET
    prefix  = var.ENVIRONMENT_SUFIX == "feat" ? "terraform/state-main" : "${var.GCP_PROJECT}/terraform/state-main"
  }
}