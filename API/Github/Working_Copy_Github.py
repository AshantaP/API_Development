from email import header
import imp
from unittest import result
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
import pandas
import io

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
    #return respo.json()
    #myjson = list_repo()
    myjson = respo.json()
    print(myjson)

    ourdata = []
    csvheader = ['ID', 'NODE_ID', 'LOGIN']

    for x in myjson:
        listing = [x['id'],x['node_id'],x['login']]
        ourdata.append(listing)
    
        df = pandas.DataFrame(ourdata)
        stream = io.StringIO()
        print(stream)
        
        df.to_csv(stream, index = False)
        response = StreamingResponse(io.StringIO(df.to_csv(index=False)), media_type="text/csv")
        print(response)
    
        response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    return response

# with open('github.csv', 'w',encoding='UTF8', newline='')as f:
#     writer = csv.writer(f)

#     writer.writerow(csvheader)
#     writer.writerows(ourdata)


# print('done')

