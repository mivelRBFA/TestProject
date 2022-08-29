gcloud scheduler jobs create http timestamp_in_BQ_job
    --schedule "*/5 * * * *"
    --uri "http://127.0.0.1:8000/file_to_bucket"
    --http-method GET