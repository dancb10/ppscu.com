### Networking ###
variable "admin_state_up" { default = "true"}
variable "network_name" {}
variable "subnet_name" {}
variable "subnet_cidr" {}
variable "ip_version" { default = "4"}

resource "openstack_networking_network_v2" "network" {
  name           = "${var.network_name}"
  admin_state_up = "${var.admin_state_up}"
}
resource "openstack_networking_subnet_v2" "subnet" {
  name       = "${var.subnet_name}"
  network_id = "${openstack_networking_network_v2.network.id}"
  cidr       = "${var.subnet_cidr}"
  ip_version = "${var.ip_version}"
}

output "network_id" {
  value = "${openstack_networking_network_v2.network.id}"
}

output "subnet_id" {
  value = "${openstack_networking_subnet_v2.subnet.id}"
}


