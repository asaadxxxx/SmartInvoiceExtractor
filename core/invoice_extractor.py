import re

from core.location_parser import LocationParser


class InvoiceExtractor:

    def __init__(self, words):

        self.words = words
        self.parser = LocationParser(words)

    def find_by_pattern(self, pattern):

        regex = re.compile(pattern)

        for word in self.words:

            text = word["text"].strip()

            if regex.fullmatch(text):
                return text

        return None

    def extract(self):

        data = {}

        # رقم ضريبي (15 رقم)
        data["supplier_vat"] = self.find_by_pattern(r"\d{15}")

        # تاريخ
        data["invoice_date"] = self.find_by_pattern(
            r"\d{1,2}[/-]\d{1,2}[/-]\d{2,4}"
        )

        # رقم الفاتورة (3 إلى 10 أرقام)
        data["invoice_number"] = self.find_by_pattern(
            r"\d{3,10}"
        )

        # إجمالي أو مبلغ
        data["total"] = self.find_by_pattern(
            r"\d+\.\d+"
        )

        return data