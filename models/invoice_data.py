from dataclasses import dataclass


@dataclass
class InvoiceData:

    supplier: str = ""

    vat_number: str = ""

    invoice_number: str = ""

    invoice_date: str = ""

    subtotal: float = 0.0

    vat_amount: float = 0.0

    total: float = 0.0

    source_file: str = ""