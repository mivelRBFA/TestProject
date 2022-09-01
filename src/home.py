from datetime import datetime, timedelta
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi import Request

from main import app


@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    now = datetime.now() + timedelta(hours=2)
    return {"hello": "world", "date": now}
    return templates.TemplateResponse("Homepage.html")
