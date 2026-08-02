import re

from models.invoice_data import InvoiceData


class InvoiceParser:

    def parse(self, text: str):

        invoice = InvoiceData()

        invoice.supplier = self.extract_supplier(text)

        invoice.vat_number = self.extract_vat(text)

        invoice.invoice_number = self.extract_invoice_number(text)

        invoice.invoice_date = self.extract_date(text)

        invoice.total = self.extract_total(text)

        invoice.vat_amount = self.extract_vat_amount(text)

        invoice.subtotal = max(
            invoice.total - invoice.vat_amount,
            0
        )

        return invoice

    def extract_supplier(self, text):

        lines = [
            x.strip()
            for x in text.splitlines()
            if x.strip()
        ]

        if lines:
            return lines[0]

        return ""

    def extract_vat(self, text):

        patterns = [

            r"\b3\d{14}\b",

            r"VAT\s*:?[\s]*(\d+)",

            r"الرقم الضريبي\s*:?[\s]*(\d+)"
        ]

        for pattern in patterns:

            m = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if m:

                return m.group(0)

        return ""

    def extract_invoice_number(self, text):

        patterns = [

            r"Invoice\s*No\.?\s*:?\s*([A-Za-z0-9\-]+)",

            r"رقم الفاتورة\s*:?\s*([A-Za-z0-9\-]+)"
        ]

        for pattern in patterns:

            m = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if m:

                return m.group(1)

        return ""

    def extract_date(self, text):

        m = re.search(

            r"\d{2}[/-]\d{2}[/-]\d{4}",

            text
        )

        if m:

            return m.group(0)

        return ""

    def extract_total(self, text):

        patterns = [

            r"Total\s*:?\s*([\d.,]+)",

            r"الإجمالي\s*:?\s*([\d.,]+)"
        ]

        for pattern in patterns:

            m = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if m:

                return float(
                    m.group(1).replace(",", "")
                )

        return 0

    def extract_vat_amount(self, text):

        patterns = [

            r"VAT\s*:?\s*([\d.,]+)",

            r"ضريبة\s*:?\s*([\d.,]+)"
        ]

        for pattern in patterns:

            m = re.search(
                pattern,
                text,
                re.IGNORECASE
            )

            if m:

                return float(
                    m.group(1).replace(",", "")
                )

        return 0