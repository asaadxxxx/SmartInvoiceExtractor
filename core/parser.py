import re
from models.invoice_data import InvoiceData


class InvoiceParser:

    def parse(self, text: str) -> InvoiceData:

        invoice = InvoiceData()

        invoice.invoice_number = self.extract_invoice_number(text)
        invoice.invoice_date = self.extract_date(text)
        invoice.vat_number = self.extract_supplier_vat(text)
        invoice.total = self.extract_total(text)
        invoice.vat_amount = self.extract_vat(text)
        invoice.subtotal = self.extract_subtotal(text)
        invoice.supplier = self.extract_supplier(text)

        return invoice

    # -------------------------

    def extract_invoice_number(self, text):

        patterns = [
            r"رقم الفاتورة\s*[:\-]?\s*(\d+)",
            r"Invoice\s*No\.?\s*[:\-]?\s*([A-Za-z0-9\-]+)",
        ]

        for pattern in patterns:

            m = re.search(pattern, text, re.IGNORECASE)

            if m:
                return m.group(1).strip()

        return ""

    # -------------------------

    def extract_date(self, text):

        m = re.search(r"\d{2}/\d{2}/\d{4}", text)

        if m:
            return m.group()

        return ""

    # -------------------------

    def extract_supplier_vat(self, text):

        vats = re.findall(r"\b3\d{14}\b", text)

        if vats:
            return vats[0]

        return ""

    # -------------------------

    def extract_supplier(self, text):

        lines = text.splitlines()

        for line in lines:

            if "شركة" in line:

                if len(line) < 80:

                    return line.strip()

        return ""

    # -------------------------

    def extract_subtotal(self, text):

        m = re.search(
            r"NET\s*TOTAL.*?([\d,]+\.\d+)",
            text,
            re.IGNORECASE | re.DOTALL,
        )

        if m:
            return m.group(1).replace(",", "")

        return ""

    # -------------------------

    def extract_vat(self, text):

        m = re.search(
            r"VAT\s*15%.*?([\d,]+\.\d+)",
            text,
            re.IGNORECASE | re.DOTALL,
        )

        if m:
            return m.group(1).replace(",", "")

        return ""

    # -------------------------

    def extract_total(self, text):

        m = re.search(
            r"Balance.*?([\d,]+\.\d+)",
            text,
            re.IGNORECASE | re.DOTALL,
        )

        if m:
            return m.group(1).replace(",", "")

        return ""