import tempfile
import zoneinfo
from datetime import datetime

from google.cloud import storage  # type: ignore

from main import app


@app.post("/file_to_bucket")
async def upload_file():
    a = zoneinfo.ZoneInfo("Europe/Brussels")
    now = datetime.now()
    now_bxl = now.astimezone(a)
    storage_client = storage.Client()
    my_bucket = storage_client.get_bucket("rbfa-workshop-sandboxes-milanvelle")
    blob = my_bucket.blob("Timestamps/" + f"{now_bxl}")
    tf = tempfile.NamedTemporaryFile(
        mode="w+b",
        suffix=".csv",
        prefix=now.strftime("%d-%m-%y--%H-%M-%S"),
        delete=False,
    )
    tf.close()
    blob.upload_from_filename(tf.name)
    return {"temp file uploaded bucket folder that contains timestamp"}
