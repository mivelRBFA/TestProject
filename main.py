from fastapi import FastAPI
from datetime import datetime
from google.cloud import bigquery

app = FastAPI()

@app.get("/")
async def read_root():
    now = datetime.now()
    return {"hello": "world",  "date": now}

@app.get("/bq_insert_timestamp")
async def read_root():
    now = datetime.now()
    my_dict = {'Timestamp': str(now)}
    row_to_insert = [my_dict]
    bq_client = bigquery.Client()
    table = bq_client.get_table("{}.{}.{}".format("rbfa-workshop-sandboxes", "timestamps_milan", "timestamps"))
    errors = bq_client.insert_rows_json(table, row_to_insert)
    if not errors:
        return {now: "inserted in bigquery table"}
    else:
        return {now: "NOT inserted in bigquery table"}





