from datetime import datetime

from main import app


@app.get("/")
async def read_root():
    now = datetime.now()
    return {"hello": "world", "date": now}
