from dataclasses import dataclass, field
from typing import List


@dataclass
class InvoiceItem:
    description: str = ""
    quantity: float = 0.0
    unit_price: float = 0.0
    tax: float = 0.0
    total: float = 0.0


@dataclass
class InvoiceData:

    file_name: str = ""

    supplier_name: str = ""
    supplier_vat: str = ""
    supplier_cr: str = ""

    customer_name: str = ""
    customer_vat: str = ""

    invoice_number: str = ""
    invoice_date: str = ""

    subtotal: float = 0.0
    vat: float = 0.0
    total: float = 0.0

    items: List[InvoiceItem] = field(default_factory=list)

    confidence: float = 0.0

    errors: List[str] = field(default_factory=list)