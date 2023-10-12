provider "google" {
  credentials = file("/Users/jason/Desktop/personal_project/ridership-headline-project/terraform/creds.json")
  project     = var.project_id
  region      = var.region
}

resource "google_bigquery_dataset" "dataset" {
  dataset_id  = "ridership_headline"
  description = "This dataset is about Malaysia public transport ridership record"
  location    = var.region

  labels = {
    environment = "default"
  }
}

resource "google_bigquery_table" "table" {
  dataset_id = google_bigquery_dataset.dataset.dataset_id
  table_id   = "ridership_headline_v1"

  schema = <<EOF
[
  { "name": "date", "type": "DATE" },
  { "name": "bus_rkl", "type": "INTEGER" },
  { "name": "bus_rkn", "type": "INTEGER" },
  { "name": "bus_rpn", "type": "INTEGER" },
  { "name": "rail_lrt_ampang", "type": "INTEGER" },
  { "name": "rail_mrt_kajang", "type": "INTEGER" },
  { "name": "rail_lrt_kj", "type": "INTEGER" },
  { "name": "rail_monorail", "type": "INTEGER" },
  { "name": "rail_mrt_pjy", "type": "INTEGER" },
  { "name": "rail_ets", "type": "INTEGER" },
  { "name": "rail_intercity", "type": "INTEGER" },
  { "name": "rail_komuter", "type": "INTEGER" },
  { "name": "rail_tebrau", "type": "INTEGER" },
  { "name": "ingested_at", "type": "TIMESTAMP" }
]
EOF

}
    
