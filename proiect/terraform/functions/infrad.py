#!/bin/python2.7
from ppscu import set_project
from ppscu import generate_template
import argparse
from pprint import pprint
import os
import subprocess

parser = argparse.ArgumentParser()
subparsers = parser.add_subparsers(help='commands')

pterraform = subparsers.add_parser('terraform', help='Deploy infrastructure using terraform')
pterraform.add_argument('--project', dest='project', action="store", help='project to apply terraform on')
pterraform.add_argument('--plan', dest='plan', action="store_true", help='terraform plan command')
pterraform.add_argument('--apply', dest='apply', action="store_true", help='terraform apply command')
pterraform.add_argument('--destroy', dest='destroy', action="store_true", help='terraform destroy command')
pterraform.add_argument('--get', dest='get', action="store_true", help='terraform get command')

pansible = subparsers.add_parser('ansible', help='Configure infrastructure using ansible')
pansible.add_argument('--run', dest='run', action="store_true", help='ansible run playbook')

arguments = parser.parse_args()

def terraform(project,action):
    conf_dir = set_project(project)
    os.chdir(conf_dir)
    generate_template(project)
    subprocess.call("terraform "+action,shell=True)


if arguments.project:
    project = arguments.project
    if arguments.plan:
        action = 'plan'
        terraform(project, action)
    elif arguments.apply:
        action = 'apply'
        terraform(project, action)
    elif arguments.destroy:
        action = 'destroy'
        terraform(project, action)
    elif arguments.get:
	action = 'get'
	terraform(project, action)
else:
    raise "You must specify a project"
