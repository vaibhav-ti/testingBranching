import os
import requests
import json
import sys

git_pulls_api = f"https://8000-trilogygrou-processbppl-csl0gsl8fqk.ws.trilogy.devspaces.com/resources/add_aws_resources/"
cwd =  os.getcwd()
output = ''
with open('output.json') as f:
   output = json.load(f)

resources = ''
with open('resources.json') as f:
   resources = json.load(f)

payload = {
    "output":  json.dumps(output),
    "branch": sys.argv[2],
    "resources": json.dumps(resources),
    "repository": sys.argv[1],
    "private_rsa_key": sys.argv[3]
}


r = requests.post(
    git_pulls_api,
    headers={"content-type": "application/json"},
    data=json.dumps(payload))
    