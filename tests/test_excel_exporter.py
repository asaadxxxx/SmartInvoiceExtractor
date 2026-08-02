from core.excel_exporter import ExcelExporter
from models.invoice_data import InvoiceData

data = []

for i in range(3):

    inv = InvoiceData()

    inv.source_file = f"invoice_{i}.pdf"
    inv.supplier = "شركة المنصور للمقاولات"
    inv.vat_number = "300123456789003"
    inv.invoice_number = f"INV-{100+i}"
    inv.invoice_date = "02/08/2026"
    inv.subtotal = 100
    inv.vat_amount = 15
    inv.total = 115

    data.append(inv)

ExcelExporter().export(
    data,
    "output/test.xlsx"
)

print("Excel OK")