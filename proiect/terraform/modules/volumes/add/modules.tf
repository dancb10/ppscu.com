variable volume_region {}
variable volume_count {}
variable compute_instances {}
variable volume_ids {}

resource "openstack_blockstorage_volume_attach_v2" "attach_volumes" {
  compute_id = "${element(split(",", var.compute_instances), count.index)}"
  volume_id = "${element(split(",", var.volume_ids), count.index)}"
  region = "${var.volume_region}"
  count = "${var.volume_count}"
}