import requests

home = "https://svc-milanvelle-dot-rbfa-workshop-sandboxes.ew.r.appspot.com"
één = "https://svc-milanvelle-dot-rbfa-workshop-sandboxes.ew.r.appspot.com/bq_insert_timestamp"
twee = (
    "https://svc-milanvelle-dot-rbfa-workshop-sandboxes.ew.r.appspot.com/file_to_bucket"
)
drie = "https://svc-milanvelle-dot-rbfa-workshop-sandboxes.ew.r.appspot.com/update_entity_in_datastore"


def call_all_endpoints(request):
    r = requests.get(url=home)
    data = r.json()
    datum = data["date"]


    r2 = requests.put(url=drie)
    print(r2)

    r3 = requests.post(url=één)
    print(r3)

    r4 = requests.post(url=twee)
    print(r4)
    return "functions called on: \n" + datum
