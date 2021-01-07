#!/usr/bin/env python
import json
import argparse
import strgen
import random
import requests
from pprint import pprint

url_user = "http://localhost:8080/user/login"
url_group = "http://localhost:8082/group/create"
cred_file = "credentials.txt"

parser = argparse.ArgumentParser(description='Create Kubechat groups')
parser.add_argument('--community_id', dest='community_id', type=str,
                    help='List of community_id where to create groups', required=True)
parser.add_argument('--no_groups', dest='no_groups', type=int,
                    help='Number of groups to create in each community', required=True)
args = parser.parse_args()
communities_id = [str(community_id) for community_id in args.community_id.split(',')]


def get_token(data, url):
    header = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=header)
    return json.loads(r.content)['token']


def generate_data(community_id):
    data = {
        "community_id": community_id,
        "name": strgen.StringGenerator("[a-zA-Z0-9]{1:100}").render(),
        "description": strgen.StringGenerator("[a-zA-Z0-9]{1:200}").render(),
        "type": "democratic",
        "visibility": "public",
        "labels": [str(strgen.StringGenerator("[a-zA-Z]{1:20}").render()) for _ in
                   range(1, random.randint(1, 20))],
        "plabels": [str(strgen.StringGenerator("[a-zA-Z]{1:20}").render()) for _ in
                    range(1, random.randint(1, 20))]
    }
    return data


def call_api(data, community_id, url, headers):
    pprint("adding group:{} to community_id:{}".format(data["name"], community_id))
    r = requests.post(url, data=json.dumps(data), headers=headers)
    if r.status_code is 200:
        print("success, added group {} in community_id: {}".format(data["name"], community_id))
    else:
        print("problem:{}, status code:".format(r.content, r.status_code))


def extract_credentials(cred_file):
    with open(cred_file, 'r') as f:
        credentials = json.load(f)
        number = random.randint(0, len(credentials) - 1)
        cred = credentials[list(credentials.keys())[number]]
        return {
            "email": cred["email"],
            "password": cred["password"]
        }



for community_id in communities_id:
    for _ in range(args.no_groups):
        cred = extract_credentials(cred_file)
        token = get_token(cred, url_user)
        headers = {'content-type': 'application/json', 'Authorization': token}
        call_api(generate_data(community_id), community_id, url_group, headers)
