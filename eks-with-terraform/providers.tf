provider "aws" {
  region = "us-west-2" 
}

terraform {
  backend "s3" {
    bucket                  = "terraform-s3-state"
    key                     = "state/terraform.tfstate"
    region                  = "us-west-2"
    shared_credentials_file = "~/.aws/credentials"
  }
}