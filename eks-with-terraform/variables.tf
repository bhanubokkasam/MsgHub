variable "region" {
  default = "us-west-2"
}

variable "cluster_name" {
  default = "eks-cluster"
}

variable "node_group_name" {
  default = "eks-nodes"
}

variable "desired_capacity" {
  default = 2
}

variable "min_size" {
  default = 1
}

variable "max_size" {
  default = 3
}

variable "instance_type" {
  default = "t3.micro"  
}

variable "vpc_name" {
  default = "eks-vpc"  
}

variable "vpc_cidr" {
  default = "10.0.0.0/16"  
}

variable "availability_zones" {
  type        = list(string)
  default     = ["us-west-2a", "us-west-2b", "us-west-2c"]
}

variable "public_subnets" {
  type        = list(string)
  default     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
}

variable "private_subnets" {
  type        = list(string)
  default     = ["10.0.101.0/24", "10.0.102.0/24", "10.0.103.0/24"]
}