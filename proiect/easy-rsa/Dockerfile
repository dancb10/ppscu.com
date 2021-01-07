FROM armv7/armhf-ubuntu
MAINTAINER ppscu.com

RUN apt-get -y install easy-rsa 

RUN ln -s /usr/share/easy-rsa/ /ca

ENV EASY_RSA	/usr/share/easy-rsa
ENV KEY_CONFIG	/openssl/openssl-1.0.0.cnf


