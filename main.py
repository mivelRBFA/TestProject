from datetime import datetime

from fastapi import FastAPI
from google.cloud import bigquery, storage

app = FastAPI()


@app.get("/")
async def read_root():
    now = datetime.now()
    return {"hello": "world", "date": now}


# code to insert timestamp into bigquery table
@app.get("/bq_insert_timestamp")
async def read_root():
    now = datetime.now()
    my_dict = {"Timestamp": f"The Timestamp is {now}"}
    row_to_insert = [my_dict]
    bq_client = bigquery.Client()
    table = bq_client.get_table("rbfa-workshop-sandboxes.timestamps_milan.timestamps")
    errors = bq_client.insert_rows_json(table, row_to_insert)
    if errors == []:
        return {f"{now} inserted in bigquery table"}
    else:
        return {f"{now} not inserted in bigquery table"}


@app.get("/file_to_bucket")
async def upload_file():
    now = datetime.now()
    f = open("log.txt", "a")
    f.write(f"{now}" + "\n")
    f.close()
    storage_client = storage.Client()
    my_bucket = storage_client.get_bucket("rbfa-workshop-sandboxes-milanvelle")
    blob = my_bucket.blob("Timestamps/" + f"{now}")
    file_path = r"C:\Users\mivel.ext\Documents\PyCharm_Projecten\TestProject\log.txt"
    blob.upload_from_filename(file_path)
    return {"logfile with new timestamp uploaded to bucket"}
