#!/bin/python
import os
import argparse
import subprocess
import random
import time
import shutil
import errno
import glob

parser = argparse.ArgumentParser(description='Script for generating CA')
parser.add_argument('--clear_keys', type=str, dest='clear_keys', action="store", help='path for Ca')
parser.add_argument('--build_ca', type=str, dest='build_ca', action="store", help='build CA')
parser.add_argument('--build_inter', type=str, dest='build_inter', action="store", help='build Intermediate CA')
parser.add_argument('--gen_server', type=str, dest='gen_server', action="store", help='generate Server certificate')
parser.add_argument('--with_ca', type=str, dest='with_ca', action="store", help='generate certificate using existing CA')
parser.add_argument('--gen_dh', type=bool, dest='gen_dh', action="store", help='generate dh')
parser.add_argument('--gen_client', type=str, dest='gen_client', action="store", help='Build client certificate/key no password')
parser.add_argument('--pass', dest='gen_client_protected', action="store_true", help='Build client certificate/key with password')

args = parser.parse_args()

current_dir = os.getcwd()
keys_dir = current_dir + '/keys/'
root_ca = keys_dir + '/root-ca/'
openvpn_dir = '/docker/openvpn/conf'
database_file = keys_dir + 'index.txt'
serial_file = keys_dir + 'serial'
openssl_dir = current_dir + '/conf/'

def build_ca(ca_name):
    subprocess.call("docker run -it --rm --name ca-ppscu -v "+keys_dir+":/ca-ppscu/:Z -v "+openssl_dir+":/openssl/:Z --env-file ca_vars_file ca-ppscu /ca/pkitool --initca "+ca_name, shell=True)
    os.chdir(keys_dir)
    os.mkdir(ca_name + '/', 0600)
    shutil.move('ca.key',ca_name + '/ca.key')
    shutil.move('ca.crt',ca_name + '/ca.crt')
    print('Root CA ' +ca_name+ ' was created successfully')
    if not os.path.isfile(serial_file):
        serial = open(serial_file,'w+')
        serial.write(str('1000')+'\n')
        print('Certificates serial file created')
        serial.close
    os.chmod(serial_file, 0755)
    if not os.path.isfile(database_file):
        database = open(database_file,'w+')
        print('Certificates database file created')
        database.close
    os.chmod(database_file, 0755)    

def create_symlink(source,name):    
    try:
        os.symlink(source, name)
    except OSError, e:
        if e.errno == errno.EEXIST:
            os.remove(name)
            os.symlink(source, name)
        else:
            raise e

def build_intermediate(inter_name,with_ca):
    ca_path = keys_dir + with_ca
    ca_inter = keys_dir + inter_name

    print('Using root CA:' +with_ca+ ' with path ' +ca_path) 
    if not os.path.isdir(ca_path):
        print('Specified root CA does not exist')
        quit()
    elif os.path.isdir(ca_path):
        create_symlink(with_ca + '/ca.key', keys_dir + 'ca.key')
        create_symlink(with_ca + '/ca.crt', keys_dir + 'ca.crt')

    subprocess.call("docker run -it --rm --name ca-ppscu -v "+keys_dir+":/ca-ppscu/:Z -v "+openssl_dir+":/openssl/:Z --env-file ca_vars_file ca-ppscu /ca/pkitool --inter "+inter_name, shell=True)
    
    ca_crt = inter_name + '.crt'
    ca_csr = inter_name + '.csr'
    ca_key = inter_name + '.key'
    
    f = open(serial_file, 'r')
    sn = f.readline()
    serial_number = int(sn) - 1
    ca_sn = str(serial_number) + '.pem'
    f.close()

    if not os.path.isdir(ca_inter):
        os.mkdir(ca_inter)
        shutil.move(keys_dir + ca_crt,ca_inter +'/ca.crt')
        shutil.move(keys_dir + ca_csr,ca_inter +'/ca.csr')
        shutil.move(keys_dir + ca_key,ca_inter +'/ca.key')
        shutil.move(keys_dir + ca_sn,ca_inter+'/'+ca_sn)

def generate_server(server_name,with_ca):
    ca_path = keys_dir + with_ca
    clients_path = keys_dir + 'clients/'
    if not os.path.isdir(ca_path):
        print('Specified root CA does not exist')
        quit()
    elif os.path.isdir(ca_path):
        create_symlink(with_ca + '/ca.key', keys_dir + 'ca.key')
        create_symlink(with_ca + '/ca.crt', keys_dir + 'ca.crt')
 	
    subprocess.call("docker run -it --rm --name ca-ppscu -v "+keys_dir+":/ca-ppscu/:Z -v "+openssl_dir+":/openssl/:Z --env-file ca_vars_file ca-ppscu /ca/pkitool --server "+server_name, shell=True)
    cert_crt = server_name + '.crt'
    cert_csr = server_name + '.csr'
    cert_key = server_name + '.key'

    f = open(serial_file, 'r')
    sn = f.readline()
    serial_number = int(sn) - 1
    cert_sn = str(serial_number) + '.pem'
    f.close()

    if not os.path.isdir(clients_path):
        os.mkdir(clients_path)
    shutil.move(keys_dir + cert_crt,clients_path + cert_crt)
    shutil.move(keys_dir + cert_csr,clients_path + cert_csr)
    shutil.move(keys_dir + cert_key,clients_path + cert_key)
    shutil.move(keys_dir + cert_sn,clients_path  + cert_sn)

def generate_dh():
    subprocess.call("docker run -it --rm --name ca-ppscu -v "+keys_dir+":/ca-ppscu/:Z -v "+openssl_dir+":/openssl/:Z --env-file ca_vars_file ca-ppscu /ca/build-dh ", shell=True)

def generate_client(server_name,with_ca,protected=''):
    ca_path = keys_dir + with_ca
    clients_path = keys_dir + 'clients/'
    if not os.path.isdir(ca_path):
        print('Specified root CA does not exist')
        quit()
    elif os.path.isdir(ca_path):
        create_symlink(with_ca + '/ca.key', keys_dir + 'ca.key')
        create_symlink(with_ca + '/ca.crt', keys_dir + 'ca.crt')
    subprocess.call("docker run -it --rm --name ca-ppscu -v "+keys_dir+":/ca-ppscu/:Z -v "+openssl_dir+":/openssl/:Z --env-file ca_vars_file ca-ppscu /ca/pkitool "+protected+" "+server_name, shell=True)
    cert_crt = server_name + '.crt'
    cert_csr = server_name + '.csr'
    cert_key = server_name + '.key'
    if not os.path.isdir(clients_path):
        os.mkdir(clients_path)
    shutil.move(keys_dir + cert_crt,clients_path + cert_crt)
    shutil.move(keys_dir + cert_csr,clients_path + cert_csr)
    shutil.move(keys_dir + cert_key,clients_path + cert_key)
    
if args.build_ca:
   build_ca(args.build_ca)

if args.build_inter:
   build_intermediate(args.build_inter,args.with_ca)

if args.gen_server:
    generate_server(args.gen_server,args.with_ca)

if args.gen_dh:
    generate_dh()

if args.gen_client:
    if args.gen_client_protected:
        generate_client(args.gen_client,args.with_ca,protected='--pass')
    else:
        generate_client(args.gen_client,args.with_ca,protected='')
