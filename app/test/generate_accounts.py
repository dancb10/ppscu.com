import requests, json
import random, string


def generate_string(length):
    return ''.join(random.choice(string.ascii_lowercase) for _ in range(length))


def generate_email(length):
    user = ''.join(random.choice(string.ascii_lowercase) for _ in range(length))
    return "{}@test.com".format(user)


for user in range(10):
    body = json.dumps({"username": generate_string(10), "password": generate_string(10), "email": generate_email(10)})
    headers = {"Content-Type": "application/json"}
    r = requests.post("http://localhost:8080/account", data=body, headers=headers)
    print(r.text)
