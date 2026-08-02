import json

from core.ocr_engine import OCREngine

ocr = OCREngine()

words = ocr.read("sample_invoice.jpeg")

with open("sample.json", "w", encoding="utf-8") as f:
    json.dump(words, f, ensure_ascii=False, indent=4)

print("عدد الكلمات:", len(words))
print("تم حفظ sample.json")