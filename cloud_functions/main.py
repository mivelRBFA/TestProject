import requests

home = "https://svc-milanvelle-dot-rbfa-workshop-sandboxes.ew.r.appspot.com"
one = home + "/bq_insert_timestamp"
two = home + "/file_to_bucket"
three = home + "/update_entity_in_datastore"


def call_all_endpoints(request):
    r = requests.get(url=home)
    data = r.json()
    datum = data["date"]

    r2 = requests.put(url=three)
    print(r2)

    r3 = requests.post(url=one)
    print(r3)

    r4 = requests.post(url=two)
    print(r4)
    return "functions called on: \n" + datum
