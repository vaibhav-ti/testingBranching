import os
import requests
import json

git_pulls_api = f"https://8000-trilogygrou-processbppl-csl0gsl8fqk.ws.trilogy.devspaces.com/resources/add_aws_resources/"
cwd =  os.getcwd()
print(cwd)
output = ''
with open('package.json') as f:
   output = json.load(f)

payload = {
    "output":  json.dumps(output)
}
print(payload)

r = requests.post(
    git_pulls_api,
    headers={"content-type": "application/json"},
    data=json.dumps(payload))
    