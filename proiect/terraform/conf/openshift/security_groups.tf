resource "openstack_compute_secgroup_v2" "kubernetes_master" {
  name        = "kubernetes_master"
  description = "Kubernetes master security group"

  rule {
    from_port   = 22
    to_port     = 22
    ip_protocol = "tcp"
    cidr        = "192.168.100.0/24"
  }

  rule {
  from_port = -1
  to_port = -1
  ip_protocol = "icmp"
  cidr = "192.168.100.0/24"
  }
}

resource "openstack_compute_secgroup_v2" "kubernetes_node" {
  name        = "kubernetes_node"
  description = "Kubernetes node security group"

  rule {
    from_port   = 22
    to_port     = 22
    ip_protocol = "tcp"
    cidr        = "192.168.100.0/24"
  }

  rule {
    from_port = -1
    to_port = -1
    ip_protocol = "icmp"
    cidr = "192.168.100.0/24"
  }
}