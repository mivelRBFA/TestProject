import zoneinfo
from datetime import datetime

from google.cloud import datastore

from main import app


@app.put("/update_entity_in_datastore")
async def update_entity_datastore():
    a = zoneinfo.ZoneInfo("Europe/Brussels")
    now = datetime.now()
    now_bxl = now.astimezone(a)
    client = datastore.Client()
    kind = "Task"
    name = "Timestamp"
    timestamp_key = client.key(kind, name)
    timestamp = datastore.Entity(key=timestamp_key)
    timestamp["Timestamp"] = f"{now_bxl}"
    client.put(timestamp)
    return {"entity updated to " + f"{now_bxl}"}
