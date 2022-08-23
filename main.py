from fastapi import FastAPI
from datetime import datetime
#from google.cloud import scheduler_v1
from google.cloud import bigquery
import os
from google.cloud import storage

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


#VOLG DEZE LINK: https://www.bing.com/videos/search?q=google+cloud+storage+upload+file+in+API&docid=608052629504462532&mid=E4F3473B3320A2994179E4F3473B3320A2994179&view=detail&FORM=VIRE
@app.get("/file_to_bucket")
async def read_root():
    now = datetime.now()

    #new txtfile
    with open('log_timestamps.txt', 'w') as f:
        f.write(str(now)+'\n')

    storage_client = storage.Client()
    my_bucket = storage_client.get_bucket('rbfa-workshop-sandboxes-milanvelle')
    blob = my_bucket.blob('log_timestamps')
    file_path = r'C:\Users\mivel.ext\Documents\PyCharm_Projecten\TestProject\log_timestamps'
    blob.upload_from_filename(file_path)
    return {"file uploaded to bucket"}


