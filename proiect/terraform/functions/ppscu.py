import yaml
from jinja2 import Environment, FileSystemLoader, Template, PackageLoader
from pprint import pprint
import os

def set_project(project):
    path = "../conf/"+ str(project) + "/"
    for i in os.listdir(path):
        for root, dirs, files in os.walk(path):
            if 'conf.yaml' in files:
                return path
    raise Exception("Project "+str(project)+" not found")

def generate_template(project):
    try:
        variables = yaml.load(file('conf.yaml', 'r'))
        env = Environment(loader=FileSystemLoader('./'))
        template = env.get_template("main.tf.j2")
        output = open("main.tf", "w")
        output.write(template.render(var=variables, trim_blocks=True, lstrip_blocks=True))
    except yaml.YAMLError as exception:
        print("Encountered: "+exception)
