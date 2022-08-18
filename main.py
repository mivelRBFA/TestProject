from fastapi import FastAPI
from datetime import datetime

app = FastAPI()


@app.get("/")
def read_root():
    now = datetime.now()
    return {"hello": "world",  "date": now}


def callback():
    print('callback triggered')






