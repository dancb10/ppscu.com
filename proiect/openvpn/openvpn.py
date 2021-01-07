#!/bin/python
import subprocess
import argparse
import os

parser = argparse.ArgumentParser(description='Script for generating CA')

parser.add_argument('--image-name', type=str, dest='image_name', action="store", help='OpenVPN Image name')
parser.add_argument('--build', dest='image_build', action="store_true", help='Create OpenVPN image')
parser.add_argument('--destroy', dest='image_destroy', action="store_true", help='Destroy OpenVPN image')

parser.add_argument('--name', type=str, dest='openvpn_name', action="store", help='OpenVPN container name')
parser.add_argument('--create', dest='openvpn_create', action="store_true", help='create OpenVPN server in docker container')
parser.add_argument('--start', dest='openvpn_start', action="store_true", help='start OpenVPN server')
parser.add_argument('--stop', dest='openvpn_stop', action="store_true", help='stop OpenVPN server')

args = parser.parse_args()

current_dir = os.getcwd()

openvpn_dir = current_dir + '/openvpn'
openvpn_certs_dir = openvpn_dir + '/certs'

def build(image_name):
    subprocess.call("docker build -t "+image_name+" "+current_dir+" --quiet", shell=True)

def create(openvpn_name,image_name):
    subprocess.call("docker run -d --name "+openvpn_name+" --privileged -v "+openvpn_dir+":/vpn-ppscu/:Z -p 1194:1194/udp "+image_name, shell=True)

def start(openvpn_name):
    subprocess.call("docker start "+openvpn_name, shell=True)

def stop(openvpn_name):
    subprocess.call("docker stop "+openvpn_name, shell=True)

if args.image_build:
    if not args.image_name:
        print('You must specify image name')
        quit()
    else:
        build(args.image_name)
        quit()

if args.openvpn_create:
    if not args.image_name:
        print('You must specify what image to use for the OpenVPN server')
        quit()
    else:
        print('Creating OpenVPN server')
        create(args.openvpn_name,args.image_name)

if args.openvpn_start:
    if not args.openvpn_name:
        print('You must specify OpenVPN server name')
        quit()
    else:
        print('Starting OpenVPN server ')
        start(args.openvpn_name)

if args.openvpn_stop:
    if not args.openvpn_name:
        print('You must specify OpenVPN server name')
        quit()
    else:
        print('Stopping OpenVPN server')
        stop(args.openvpn_name)
