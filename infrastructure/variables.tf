variable "instance_type" {
    type = string
}

variable "ami_id" {
    type = string
    description = "ubuntu free tier ami: ami-044415bb13eee2391"
}

variable "aws_profile" {
    type = string
}

variable "region" {
    type = string
}

variable "key_name" {
    type = string
    description = "key name"
}


variable "project_name" {
    type = string
}

variable "availability_zone" {
    type = string
}

variable "cidr_block" {
    type = string
}

variable "public_subnet_cidr_block" {
    type = string
}

variable "route_table_cidr_block" {
    type = string
}