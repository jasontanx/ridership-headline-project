# terraform-practice

Terraform is an infrastructure as code tool that lets you build, change, and version cloud and on-prem resources safely and efficiently.

Source: https://developer.hashicorp.com/terraform/intro

For this project, terraform was implemented to help in developing the ridership table at GCP BigQuery.

Pre-requisite:
You will have to ensure that the Google credentials are created and ready 

CLI Notes:

1. To initialize working directory --> ```terraform init```
2. To rewrite Terraform configuration files to a canonical format and style --> ```terraform fmt``` 
3. To validate the configuration internally --> ```terraform validate```
4. To create an execution plan, which lets us preview the changes that Terraform plans to make to your infrastructure --> ```terraform plan```
5. To executes the actions proposed in a Terraform plan to create, update, or destroy infrastructure --> ```terraform apply```
