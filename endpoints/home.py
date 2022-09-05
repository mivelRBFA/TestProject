import zoneinfo
from datetime import datetime

from main import app


@app.get("/")
async def read_root():
    a = zoneinfo.ZoneInfo("Europe/Brussels")
    now = datetime.now()
    now_bxl = now.astimezone(a)
    return {"hello": "world", "date": now_bxl}
