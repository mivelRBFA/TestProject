from fastapi import FastAPI

app = FastAPI()
from endpoints import (bq_insert_timestamp, file_to_bucket,  # noqa: E402,F401
                       home, update_entity)
