from datetime import datetime, timedelta

from google.cloud import datastore
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from pathlib import Path

from main import app
app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/update_entity_in_datastore", response_class=HTMLResponse)
async def update_entity_datastore(request: Request):
    now = datetime.now() + timedelta(hours=2)
    client = datastore.Client()
    kind = "Task"
    name = "Timestamp"
    timestamp_key = client.key(kind, name)
    timestamp = datastore.Entity(key=timestamp_key)
    timestamp["Timestamp"] = f"{now}"
    client.put(timestamp)
    return templates.TemplateResponse("update_entity.html", {"request": request})
