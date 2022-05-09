from asyncio import streams
import imp
from urllib import response
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
import io
import pandas

app = FastAPI()
f = open("empty.dat", 'r')
secret = json.load(f)
f.close()

@app.get("/")
async def get_csv():
    #df = pandas.DataFrame dict({'col1'} : [1], 'col2' : [2]})
    df = pandas.DataFrame({'col1': [1], 'col2': [2]})
    stream = io.StringIO()
    df.to_csv(stream, index = False)
    response = StreamingResponse(io.StringIO(df.to_csv(index=False)), media_type="text/csv")
    
    response.headers["Content-Disposition"] = "attachment; filename=export.csv"
    
    return response
