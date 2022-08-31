from datetime import datetime, timedelta

from main import app


@app.get("/")
async def read_root():
    now = datetime.now() + timedelta(hours=2)
    return {"hello": "world", "date": now}
