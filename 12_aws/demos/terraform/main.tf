terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 3.27"
    }
  }

  required_version = ">= 0.14.9"
}

provider "aws" {
  profile = "default"
  region  = "us-east-1"
}

resource "aws_instance" "app_server" {
  ami           = "ami-0d5eff06f840b45e9"
  instance_type = "t2.micro"

  tags = {
    Name = "jrrickerson-demo-terraform"
    course = "LM-IEA"
    cohort = var.cohort
  }
}

resource "aws_instance" "app_server2" {
  ami           = "ami-0d5eff06f840b45e9"
  instance_type = "t3.small"

  tags = {
    Name = "jrrickerson-demo-terraform2"
    course = "LM-IEA"
  }
}

