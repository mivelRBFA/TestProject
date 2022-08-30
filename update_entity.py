from datetime import datetime

from google.cloud import datastore

from main import app


@app.get("/update_entity_in_datastore")
async def update_entity_datastore():
    now = datetime.now()
    client = datastore.Client()
    kind = "Task"
    name = "Timestamp"
    timestamp_key = client.key(kind, name)
    timestamp = datastore.Entity(key=timestamp_key)
    timestamp["Timestamp"] = f"{now}"
    client.put(timestamp)
    return {"entity updated to " + f"{now}"}
