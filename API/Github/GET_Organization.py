import imp
from flask import request
import requests as req
from typing import Optional
from fastapi import FastAPI
import json
import requests
import csv
from requests.api import head
from fastapi.responses import StreamingResponse
from io import BytesIO


app = FastAPI()
f = open("empty.dat", 'r')
secret = json.load(f)
f.close()


@app.get("/")
def root_path():
    return {"Result": {"Hello World"}}

@app.get("/organizations")
def list_repo(orgs: Optional[str] = None):
    respo = req.get("https://api.github.com/organizations", auth=("ashantap", secret['code']))
    return respo.json()
myjson = list_repo()
#print(myjson)

ourdata = []
csvheader = ['ID', 'NODE_ID', 'ISSUES_URL']

for x in myjson:
    listing = [x['id'],x['node_id'],['issues_url']]
    ourdata.append(listing)

with open('github.csv', 'w',encoding='UTF8', newline='')as f:
    writer = csv.writer(f)

    writer.writerow(csvheader)
    writer.writerows(ourdata)


print('done')
