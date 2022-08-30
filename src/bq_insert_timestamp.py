from datetime import datetime

from google.cloud import bigquery

from main import app


@app.get("/bq_insert_timestamp")
async def bq_insert():
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
