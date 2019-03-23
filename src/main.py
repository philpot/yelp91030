#!/usr/bin/env python

from yelpapi import YelpAPI
import json

from categories import top_level_categories


with open('../vault/apikey.json', 'r') as f:
    body = json.load(f)
    yelpkey = body['api_key']
    service = YelpAPI(yelpkey)

search_categories = set([c['alias'] for c in top_level_categories]) - set(['publicservicesgovt', 'religiousorgs'])

LAT = 34.1161
LONG = -118.1503

"""If term is not included the endpoint will default to searching across businesses from a small number of popular categories."""

def yelp91030(term):
    d = fetch(term=term)
    print('term: {t}'.format(t=term))
    print('fetched: {f}'.format(f=d['fetched']))
    print('kept: {k}'.format(k=d['kept']))
    catalog = d['catalog']
    fname = str(term) + '.json'
    print("writing to {n}".format(n=fname))
    with open(fname, 'w') as f:
        json.dump(catalog, f)

def fetch(latitude=LAT,
          longitude=LONG,
          zips=["91030", "91031"],
          sort_by="distance",
          radius=0,
          term=None):
    catalog = []
    fetched = 0
    kept = 0
    delta = 50
    args = {"latitude": latitude,
            "longitude": longitude,
            "sort_by": sort_by,
            "radius": radius}
    if term:
        args["term"] = term
    offset = 0
    b = service.search_query(offset=offset, limit=delta, **args)
    total = int(b["total"])
    try:
        while b and (offset < total) and offset + delta <= 1000:
            for d in b["businesses"]:
                fetched += 1
                try:
                    if d["location"]["zip_code"] in zips:
                        kept += 1
                        catalog.append(d)
                except Exception:
                    pass
            offset += delta
            b = service.search_query(offset=offset, limit=delta, **args)
    except Exception as e:
        print(e)
    return {"fetched": fetched,
            "kept": kept,
            "catalog": catalog}
