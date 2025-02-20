terraform {
  required_providers {
    google = {
      source  = "hashicorp/google"
      version = "4.51.0"
    }
  }
}

provider "google" {
  credentials = "/workspaces/DEcamp25/.ipynb_checkpoints/keys/my-credentials.json"
  project     = "decamp25"  # Update this to your actual project ID
  region      = "us-central1"
}

resource "google_storage_bucket" "decamp25" {
  name          = "green-taxi-bucket-2025"  # Compliant name
  location      = "US"

  storage_class = "STANDARD"
  uniform_bucket_level_access = true

  versioning {
    enabled = true
  }

  lifecycle_rule {
    action {
      type = "Delete"
    }
    condition {
      age = 30 // days
    }
  }

  force_destroy = true
}



resource "google_bigquery_dataset" "demo_dataset" {
  dataset_id = "demo_dataset"
  project    = "decamp25"
  location   = "US"
}