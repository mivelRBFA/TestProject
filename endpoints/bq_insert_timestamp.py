import zoneinfo
from datetime import datetime

from google.cloud import bigquery

from main import app


@app.post("/bq_insert_timestamp")
async def bq_insert():
    a = zoneinfo.ZoneInfo("Europe/Brussels")
    now = datetime.now()
    now_bxl = now.astimezone(a)
    my_dict = {"Timestamp": f"The Timestamp is {now_bxl}"}
    row_to_insert = [my_dict]
    bq_client = bigquery.Client()
    table = bq_client.get_table("rbfa-workshop-sandboxes.timestamps_milan.timestamps") # noqa
    errors = bq_client.insert_rows_json(table, row_to_insert)
    if errors == []:
        return {f"{now_bxl} inserted in bigquery table"}
    else:
        return {f"{now_bxl} not inserted in bigquery table"}
