import json

from collections import namedtuple

files = ['arts.json',
         'consultant.json',
         'corporate.json',
         'culture.json',
         'dentist.json',
         'doctor.json',
         'finance.json',
         'grocery.json',
         'legal.json',
         'medical.json',
         'professional.json',
         'realtor.json',
         'retail.json',
         'sales.json',
         'service.json',
         "spa.json",
         "beauty.json"]

files = ['../output2/arts.json',
         '../output2/consultant.json',
         '../output2/corporate.json',
         '../output2/culture.json',
         '../output2/dental.json',
         '../output2/dentist.json',
         '../output2/doctor.json',
         '../output2/finance.json',
         '../output2/grocery.json',
         '../output2/legal.json',
         '../output2/medical.json',
         '../output2/professional.json',
         '../output2/realtor.json',
         '../output2/retail.json',
         '../output2/sales.json',
         '../output2/service.json',
         '../output2/spa.json',
         '../output2/design.json',
         '../output2/graphic.json',
         '../output2/insurance.json',
         '../output2/media.json',
         '../output2/transport.json']

biz = namedtuple("biz", ["name", "display_address", "display_phone", "address1", "address2", "address3", "city", "state", "zip_code",
                         "categories", "price"])

net = set()

for filename in files:
    with open(filename, 'r') as f:
        items = json.load(f)
        for d in items:
            name = d.get('name', '')
            try:
                display_address = d['location']['display_address']
                if isinstance(display_address, list):
                    display_address = "  ".join(display_address)
            except Exception:
                display_address = ""

            display_phone = d.get('display_phone', '')

            try:
                address1 = d['location']['address1'] or ""
                if isinstance(address1, list):
                    address1 = "  ".join(address1)
            except Exception:
                address1 = ""

            try:
                address2 = d['location']['address2'] or ""
                if isinstance(address2, list):
                    address2 = "  ".join(address2)
            except Exception:
                address2 = ""

            try:
                address3 = d['location']['address3'] or ""
                if isinstance(address3, list):
                    address3 = "  ".join(address3)
            except Exception:
                address3 = ""

            try:
                city = d['location']['city']
                if isinstance(city, list):
                    city = "  ".join(city)
            except Exception:
                city = ""

            try:
                state = d['location']['state']
                if isinstance(state, list):
                    state = "  ".join(state)
            except Exception:
                state = ""

            try:
                zip_code = d['location']['zip_code']
                if isinstance(zip_code, list):
                    zip_code = "  ".join(zip_code)
            except Exception:
                zip_code = ""

            try:
                categories = d['categories']
                if isinstance(categories, list):
                    categories = ";".join([c['title'] for c in categories])
            except Exception:
                categories = ""

            try:
                price = d['price']
                if isinstance(price, list):
                    price = ";".join(price)
            except Exception:
                price = ""

            b = biz(name=name,
                    display_address=display_address,
                    display_phone=display_phone,
                    address1=address1,
                    address2=address2,
                    address3=address3,
                    city=city,
                    state=state,
                    zip_code=zip_code,
                    categories=categories,
                    price=price)
            net.add(b)
