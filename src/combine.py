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
         'service.json']

biz = namedtuple("biz", ["name", "display_address", "display_phone"])

net = set()

for filename in files:
    with open(filename, 'r') as f:
        items = json.load(f)
        for d in items:
            name = d.get('name', '')
            try:
                address = d['location']['display_address']
                if isinstance(address, list):
                    address = "  ".join(address)
            except Exception:
                address = ""
            display_phone = d.get('display_phone', '')

            b = biz(name=name, display_address=address, display_phone=display_phone)
            net.add(b)
