### Authentication ###

provider "openstack" {
  user_name   = "admin"
  tenant_name = "Openshift"
  password    = "Ubisoft2016"
  auth_url    = "http://192.168.100.100:5000/v3"
}

module "internal_network" {
  source = "../../modules/networking/network"
    network_name = "internal_network"
    admin_state_up = "true"
    subnet_name = "internal_subnet"
    subnet_cidr = "10.10.10.0/24"
}

module "openshift-router" {
  source = "../../modules/networking/router"
    router_name = "openshift-router"
    router_externalgw = "${ var.external_network_uuid }"
    router_subnetid = "${ module.internal_network.subnet_id }"
}
module "ksmaster" {
  source = "../../modules/instances"
     instance_region = "RegionOne"
     instance_domain = "ppscu"
     instance_role = "ksmaster"
     instance_count = "1"
     instance_flavor = "${lookup(var.flavor, "ksmaster" )}"
     instance_image = "${lookup(var.images, "centos7" )}"
     internal_network = "${ module.internal_network.network_id }"
     security_groups = "kubernetes_master"
     key_pair = "admin-keypair"
     floating_pool = "external_network"
}

module "ksnode" {
  source = "../../modules/instances"
     instance_region = "RegionOne"
     instance_domain = "ppscu"
     instance_role = "ksnode"
     instance_count = "2"
     instance_flavor = "${lookup(var.flavor, "ksnode" )}"
     instance_image = "${lookup(var.images, "centos7" )}"
     internal_network = "${ module.internal_network.network_id }"
     security_groups = "kubernetes_node"
     key_pair = "admin-keypair"
     floating_pool = "external_network"
}


resource "openstack_compute_keypair_v2" "admin-keypair" {
  name       = "admin-keypair"
  public_key = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQDe/UY2m24End3+8849Au+tnQJ4q/jmZ59j2Er3poePSaHwBc7xfMfAvHsihrtRpP29df1XiiBuq+m/Y29xPr1np/e9U9pQzO4h1ImGvXVjv3siMeemgEW4QhdIKbowt+EsQJJ1fpcg1bTEW4ZUwZdrHMXRmWeXmbN/Yzd8ASx2pogipS9j/wxwqepR+XUj203gteLAFMFGPYLAPQnMGrMWkxuth0k2SvwrqW+YCmVj3NjrdcKvF0bdmDozNIcO4WmM7AewFS2nL615s/nUw3KDDwMTa9RWjIle13Bty3kHQRHxFD/NHeX0yj+yTt6uD11s1fiV8HJKqrnmkdMwBAyF admin@rheltest"
}