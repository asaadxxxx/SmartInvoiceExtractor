from core.parser import InvoiceParser

with open("sample.txt", "r", encoding="utf8") as f:
    text = f.read()

invoice = InvoiceParser().parse(text)

print("=" * 40)
print("Supplier :", invoice.supplier)
print("VAT      :", invoice.vat_number)
print("Invoice  :", invoice.invoice_number)
print("Date     :", invoice.invoice_date)
print("Subtotal :", invoice.subtotal)
print("VAT Amt  :", invoice.vat_amount)
print("Total    :", invoice.total)