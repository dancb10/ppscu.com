#!/usr/bin/env python
import json
import argparse
import strgen
import random
import requests
from pprint import pprint
url_user = "http://localhost:8080/user/login"
url_thread = "http://localhost:8090/thread/create"
credentials = {
    "email": "leHiCUZyhTBUKs@kubechat.com",
    "password": "SnI3#i.^fzLey"
}

parser = argparse.ArgumentParser(description='Create Kubechat threads')
parser.add_argument('--groups_id', dest='groups_id', type=str,
                    help='List of groups_id where to create threads', required=True)
parser.add_argument('--no_threads', dest='no_threads', type=int,
                    help='Number of threads to create in each group', required=True)
args = parser.parse_args()
groups_id = [str(group_id) for group_id in args.groups_id.split(',')]


def get_token(data, url):
    header = {'content-type': 'application/json'}
    r = requests.post(url, data=json.dumps(data), headers=header)
    return json.loads(r.content)['token']


def generate_data(group_id):
    data = {
            "group_id": group_id,
            "name": strgen.StringGenerator("[a-zA-Z0-9]{1:100}").render(),
            "summary": strgen.StringGenerator("[a-zA-Z0-9]{1:200}").render(),
            "content": strgen.StringGenerator("[a-zA-Z0-9]{1:500}").render(),
            "labels": [str(strgen.StringGenerator("[a-zA-Z]{1:20}").render()) for _ in
                       range(1, random.randint(1, 20))],
            "plabels": [str(strgen.StringGenerator("[a-zA-Z]{1:20}").render()) for _ in
                        range(1, random.randint(1, 20))]
            }
    return data


def call_api(data, group_id, url):
    pprint("adding thread:{} to group:{}".format(data["name"], group_id))
    r = requests.post(url, data=json.dumps(data), headers=headers)
    if r.status_code is 200:
        print("success, added thread {} in group_id: {}".format(data["name"], group_id))
    else:
        print("problem:{}, status code:".format(r.content, r.status_code))


token = get_token(credentials, url_user)
headers = {'content-type': 'application/json', 'Authorization': token}
for group_id in groups_id:
    for _ in range(args.no_threads):
        call_api(generate_data(group_id), group_id, url_thread)
