#!/usr/bin/env python
import json
import argparse
import strgen
import random
import time
import requests

user_user_create = "http://localhost:8080/user/create"
url_user_login = "http://localhost:8080/user/login"
cred_file = "credentials.txt"
with open(cred_file) as f:
    try:
        credentials = json.load(f)
    except Exception as e:
        credentials = json.loads("{}")

parser = argparse.ArgumentParser(description='Create Kubechat users')
parser.add_argument('--no-users', dest='no_users', type=int,
                    help='Number of users to create', required=True)
args = parser.parse_args()


def get_token(data, url):
    header = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=header)
    return json.loads(r.content)['token']


def generate_data():
    data = {
        "firstname": strgen.StringGenerator("[a-zA-Z]{1:30}").render(),
        "lastname": strgen.StringGenerator("[a-zA-Z]{1:30}").render(),
        "password":  strgen.StringGenerator("[\l\d\p]{7:30}").render(),
        "email": strgen.StringGenerator("[\l]{7:20}@kubechat.com").render(),
    }
    return data


def create_users(file, url):
    header = {'content-type': 'application/json'}
    no = 0
    with open(file, 'r') as file:
        local_cred = json.load(file)
        for user in local_cred:
            if no >= 10:
                time.sleep(1)
                no = 0
            no += 1
            data = local_cred[user]
            r = requests.post(url, data=json.dumps(data), headers=header)
            if r.status_code is 200:
                print("success, created user: {}".format(user))
            else:
                print("problem:{}, status code:".format(r.content, r.status_code))


def check_credentials(email, cred):
    if email in cred:
        return True
    return False


def generate_credentials(number, file):
    for nr in range(number):
        user = generate_data()
        while check_credentials(user["email"], credentials):
            user = generate_data()
        credentials[user["email"]] = user
    open(file, 'w').close()
    save_credentials(credentials, file)


def save_credentials(cred, file_name):
    with open(file_name, 'a') as f:
        json.dump(cred, f, indent=4)
        print("Credentials written to disk")


generate_credentials(args.no_users, cred_file)
create_users(cred_file, user_user_create)
