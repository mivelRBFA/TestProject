from fastapi import FastAPI
from datetime import datetime
import os
app = FastAPI()

credential_path = "C:\\Users\mivel.ext\Documents\cred_GCP_serviceacc.json"
os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = credential_path


@app.get("/")
async def read_root():
    now = datetime.now()
    return {"hello": "world",  "date": now}






