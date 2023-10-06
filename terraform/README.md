# terraform - BQ Table Creation

Terraform is an infrastructure as code tool that lets you build, change, and version cloud and on-prem resources safely and efficiently.

Source: https://developer.hashicorp.com/terraform/intro

For this project, terraform was implemented to help in developing the ridership table at GCP BigQuery.

Pre-requisite:
- You will have to ensure that the Google credentials are created and ready
- Google Service Account to be created (Example shown below)


A sample Google Application Credentials file in JSON format:
```
{
  "type": "service_account",
  "project_id": "my-project-id",
  "private_key_id": "my-private-key-id",
  "private_key": "my-private-key",
  "client_email": "my-client-email@my-project-id.iam.gserviceaccount.com",
  "client_id": "my-client-id",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/my-project-id@appspot.gserviceaccount.com",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/my-client-email@my-project-id.iam.gserviceaccount.com"
}
```

CLI Notes:

1. To initialize working directory --> ```terraform init```
2. To rewrite Terraform configuration files to a canonical format and style --> ```terraform fmt``` 
3. To validate the configuration internally --> ```terraform validate```
4. To create an execution plan, which lets us preview the changes that Terraform plans to make to your infrastructure --> ```terraform plan```
5. To executes the actions proposed in a Terraform plan to create, update, or destroy infrastructure --> ```terraform apply```
