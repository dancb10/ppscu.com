variable floating_pool {}
variable instance_id {}
variable instance_count {}

resource "openstack_networking_floatingip_v2" "floating_pool" {
  pool = "${var.floating_pool}"
}

resource "openstack_compute_floatingip_associate_v2" "fip_1" {
  floating_ip = "${openstack_networking_floatingip_v2.floating_pool.address}"
  instance_id = "${var.instance_id}"
  count = "${var.instance_count}"
}