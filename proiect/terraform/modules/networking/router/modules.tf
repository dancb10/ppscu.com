variable "router_name" {}
variable "router_externalgw" {}
variable "router_subnetid" {}

resource "openstack_networking_router_v2" "router" {
  name             = "${var.router_name}"
  external_gateway = "${var.router_externalgw}"
}

resource "openstack_networking_router_interface_v2" "router_interface_1" {
  router_id = "${openstack_networking_router_v2.router.id}"
  subnet_id = "${var.router_subnetid}"
}