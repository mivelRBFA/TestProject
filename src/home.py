from datetime import datetime, timedelta
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from pathlib import Path

from main import app
app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    now = datetime.now() + timedelta(hours=2)
    #return {"hello": "world", "date": now}
    return templates.TemplateResponse("Homepage.html", {"request": request})
