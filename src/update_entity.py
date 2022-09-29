from datetime import datetime, timedelta

from google.cloud import datastore
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from pathlib import Path
import zoneinfo

from main import app
app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/update_entity_in_datastore", response_class=HTMLResponse)
async def update_entity_datastore(request: Request):
    a = zoneinfo.ZoneInfo("Europe/Brussels")
    now_dt = datetime.now()
    now = now_dt.astimezone(a)
    client = datastore.Client()
    kind = "Task"
    name = "Timestamp"
    timestamp_key = client.key(kind, name)
    timestamp = datastore.Entity(key=timestamp_key)
    timestamp["Timestamp"] = f"{now}"
    client.put(timestamp)
    @app.get("/timestamp_get_update")
    async def timestamp_get_update(request: Request):
        now_str = str(now.hour)+':'+str(now.minute)+':'+str(now.second)+' on '+str(now.day)+'/'+str(now.month)+'/'+str(now.year)
        return now_str

    return templates.TemplateResponse("update_entity.html", {"request": request})

