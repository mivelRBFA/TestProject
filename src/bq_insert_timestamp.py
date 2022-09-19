from datetime import datetime, timedelta

from google.cloud import bigquery
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from pathlib import Path

from main import app
app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/bq_insert_timestamp", response_class=HTMLResponse)
async def bq_insert(request: Request):
    now = datetime.now() + timedelta(hours=2)
    my_dict = {"Timestamp": f"The Timestamp is {now}"}
    row_to_insert = [my_dict]
    bq_client = bigquery.Client()
    table = bq_client.get_table("rbfa-workshop-sandboxes.timestamps_milan.timestamps")
    errors = bq_client.insert_rows_json(table, row_to_insert)
    if errors == []:
        return templates.TemplateResponse("bq_insert_timestamp.html", {"request": request})
    else:
        return templates.TemplateResponse("bq_insert_timestamp_error.html", {"request": request})
