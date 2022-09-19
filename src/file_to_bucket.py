import tempfile
from datetime import datetime, timedelta

from google.cloud import storage
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi import Request
from pathlib import Path

from main import app
app.mount("/static", StaticFiles(directory=Path(__file__).parent.parent.absolute() / "static"), name="static")
templates = Jinja2Templates(directory="templates")

@app.get("/file_to_bucket", response_class=HTMLResponse)
async def upload_file(request: Request):
    now = datetime.now() + timedelta(hours=2)
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
    return templates.TemplateResponse("file_to_bucket.html", {"request": request})
