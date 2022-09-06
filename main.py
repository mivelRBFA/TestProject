from fastapi import FastAPI


app = FastAPI()
from endpoints import bq_insert_timestamp, file_to_bucket, home, update_entity
