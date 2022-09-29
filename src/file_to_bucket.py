import tempfile
from datetime import datetime, timedelta

from google.cloud import storage
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from pathlib import Path
import zoneinfo

from main import app
app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/file_to_bucket", response_class=HTMLResponse)
async def upload_file(request: Request):
    a = zoneinfo.ZoneInfo("Europe/Brussels")
    now_dt = datetime.now()
    now = now_dt.astimezone(a)
    storage_client = storage.Client()
    my_bucket = storage_client.get_bucket("rbfa-workshop-sandboxes-milanvelle")
    blob = my_bucket.blob("Timestamps/" + f"{now}")
    tf = tempfile.NamedTemporaryFile(
        mode="w+b",
        suffix=".csv",
        prefix=now.strftime("%d-%m-%y--%H-%M-%S"),
        delete=False,
    )
    tf.close()
    blob.upload_from_filename(tf.name)
    @app.get("/timestamp_get_ftb")
    async def timestamp_get_ftb(request: Request):
        now_str = str(now.hour) + ':' + str(now.minute) + ':' + str(now.second) + ' on ' + str(now.day) + '/' + str(now.month) + '/' + str(now.year)
        return now_str

    return templates.TemplateResponse("file_to_bucket.html", {"request": request})
