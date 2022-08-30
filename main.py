from fastapi import FastAPI

app = FastAPI()
from src import bq_insert_timestamp, file_to_bucket, home, update_entity

home.read_root()
bq_insert_timestamp.bq_insert()
file_to_bucket.upload_file()
update_entity.update_entity_datastore()
