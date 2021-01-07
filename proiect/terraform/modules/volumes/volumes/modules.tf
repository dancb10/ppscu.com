### Volumes ###
variable "region" {}
variable "volume_description" {}
variable "volume_size" {}
variable "volume_count" {}
variable "volume_domain" {}
variable "volume_region" {}
variable "volume_name" {}
variable "instance_role" {}

resource "openstack_blockstorage_volume_v2" "volumes" {
  region      = "${ var.region }"
  name        = "${format("${ var.volume_region }-volume-${ var.volume_domain }-${ var.instance_role }-${ var.volume_name }-%02d", count.index+1)}"
  description = "${ var.volume_description }"
  size        = "${ var.volume_size }"
  count       = "${ var.volume_count }"
}

output volumes_ids {
  value = "${join(",", openstack_blockstorage_volume_v2.volumes.*.id)}"
}