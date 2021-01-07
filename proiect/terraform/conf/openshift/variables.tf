variable "flavor" {
  type = "map"
  default = {
    "ksmaster" = "24e308a2-78cc-4f7e-8d5d-1247beb4636e"
    "ksnode" = "aedad9f5-fae2-440b-bae1-f1d1b987868b"
  }
}

variable "images" {
  type = "map"
  default = {
    "centos7" = "7d74d146-1259-4107-9bfa-158697c8c7e7"
  }
}

variable "floating_pool" {
  type = "string"
  default = "external_network"
}

variable "external_network_uuid" {
  type = "string"
  default = "72d9b479-9998-4cf4-aaba-bab7e6f3d9e5"
}
