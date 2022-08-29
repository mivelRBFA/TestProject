gcloud scheduler jobs create http timestamp_in_BQ_job \
    --schedule every 5 minutes \
    --uri "http://myproject/my-url.com" \
    --http-method GET