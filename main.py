from fastapi import FastAPI
from datetime import datetime
from google.cloud import bigquery
from google.cloud import storage

app = FastAPI()

@app.get("/")
async def read_root():
    now = datetime.now()
    return {"hello": "world",  "date": now}


#code to insert timestamp into bigquery table
@app.get("/bq_insert_timestamp")
async def insert_timestamp():
    now = datetime.now()
    my_dict = {'Timestamp': f"(now)"}
    row_to_insert = [my_dict]
    bq_client = bigquery.Client()
    table = bq_client.get_table("{}.{}.{}".format("rbfa-workshop-sandboxes", "timestamps_milan", "timestamps"))
    errors = bq_client.insert_rows_json(table, row_to_insert)
    if errors == []:
        return {now: "inserted in bigquery table"}
    else:
        return {now: "not inserted in bigquery table"}


@app.get("/file_to_bucket")
async def upload_file():
    now = datetime.now()
    f = open("log.txt", 'a')
    f.write(str(now)+"\n")
    print('written')
    f.close()
    storage_client = storage.Client()
    my_bucket = storage_client.get_bucket('rbfa-workshop-sandboxes-milanvelle')
    blob = my_bucket.blob('Timestamps/log')
    file_path = r'C:\Users\mivel.ext\Documents\PyCharm_Projecten\TestProject\log.txt'
    blob.upload_from_filename(file_path)
    return {"logfile with new timestamp uploaded to bucket"}




