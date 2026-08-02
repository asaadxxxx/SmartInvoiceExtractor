import json

from core.location_parser import LocationParser

with open("sample.json", "r", encoding="utf-8") as f:
    words = json.load(f)

parser = LocationParser(words)

fields = [
    "invoice_number",
    "invoice_date",
    "supplier_vat",
    "customer_vat",
    "total",
    "vat",
    "subtotal",
]

for field in fields:

    print("=" * 60)
    print(field)

    value = parser.extract_right_value(field)

    if value:
        print("Value:", value)
    else:
        print("Not Found")