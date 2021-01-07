variable instance_region {}
variable instance_domain {}
variable instance_role {}
variable instance_count {}
variable instance_flavor {}
variable instance_image {}
variable key_pair { default = "" }
variable internal_network {}
variable security_groups { default = "default"}
variable floating_pool {}

resource "openstack_compute_floatingip_v2" "floating" {
  count = "${var.instance_count}"
  region = "${var.instance_region}"
  pool = "${var.floating_pool}"
}

resource "openstack_compute_instance_v2" "instance" {
  name            = "${format("${var.instance_region}-${var.instance_domain}-${var.instance_role}-%02d", count.index+1)}"
  count           = "${var.instance_count}"
  image_id        = "${var.instance_image}"
  flavor_id       = "${var.instance_flavor}"
  key_pair        = "${var.key_pair}"
  security_groups = ["default"]

  network {
    uuid = "${var.internal_network}"
    floating_ip = "${element(openstack_compute_floatingip_v2.floating.*.address, count.index)}"
  }
}

output "instance_id" {
   value = "${join(",", openstack_compute_instance_v2.instance.*.id)}"
}

output "floating_ip" {
  value = ["${openstack_compute_floatingip_v2.floating.*.address}"]
}