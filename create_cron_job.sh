gcloud scheduler jobs create http job_5m_endpoint_call --location=europe-west --schedule="*/5 * * * *" --uri=https://svc-milanvelle-dot-rbfa-workshop-sandboxes.ew.r.appspot.com/update_entity_in_datastore --http-method GET