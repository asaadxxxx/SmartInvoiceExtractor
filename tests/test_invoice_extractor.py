import json

from core.invoice_extractor import InvoiceExtractor

with open("sample.json", "r", encoding="utf-8") as f:
    words = json.load(f)

extractor = InvoiceExtractor(words)

result = extractor.extract()

print("=" * 60)

for key, value in result.items():
    print(f"{key}: {value}")