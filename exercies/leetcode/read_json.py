import json

with open('text.json', 'r') as f:
    json = json.load(f)
    for key in json:
        print("{}:{}".format(key, json[key]))
