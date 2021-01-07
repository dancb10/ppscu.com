variable "scgroup_name" {}
variable "scgroup_description" {}
variable "scgroup_direction" {}
variable "scgroup_ethertype" { default = "IPv4" }
variable "scgroup_protocol" {}
variable "scgroup_port_range_min" {}
variable "scgroup_port_range_max" {}
variable "scgroup_remote_ip_prefix" {}

resource "openstack_networking_secgroup_v2" "scgroup" {
  name        = "${ var.scgroup_name }"
  description = "${ var.scgroup_description }"
}

resource "openstack_networking_secgroup_rule_v2" "scgroup_rule" {
  direction         = "${ var.scgroup_direction }"
  ethertype         = "${ var.scgroup_ethertype }"
  protocol          = "${ var.scgroup_protocol }"
  port_range_min    = "${ scgroup_port_range_min }"
  port_range_max    = "${ scgroup_port_range_max }"
  remote_ip_prefix  = "${ scgroup_remote_ip_prefix }"
  security_group_id = "${openstack_networking_secgroup_v2.security_group.id}"
}