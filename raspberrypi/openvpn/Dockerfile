FROM armv7/armhf-ubuntu
MAINTAINER ppscu.com

RUN apt-get update -q
RUN apt-get install -y net-tools openvpn iptables socat curl 
RUN apt-get install -y python vim

ADD ./openvpn.run /bin

VOLUME /vpn-ppscu

EXPOSE 1194/udp

CMD openvpn.run
