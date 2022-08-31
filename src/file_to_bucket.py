import tempfile
from datetime import datetime, timedelta

from google.cloud import storage

from main import app


@app.get("/file_to_bucket")
async def upload_file():
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
    return {"temp file uploaded bucket folder that contains timestamp"}
