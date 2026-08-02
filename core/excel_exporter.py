from openpyxl import Workbook
from openpyxl.styles import Font


class ExcelExporter:

    def export(self, invoices, output_file):

        wb = Workbook()

        ws = wb.active

        ws.title = "Invoices"

        headers = [
            "اسم الملف",
            "المورد",
            "الرقم الضريبي",
            "رقم الفاتورة",
            "التاريخ",
            "قبل الضريبة",
            "الضريبة",
            "الإجمالي",
        ]

        ws.append(headers)

        for cell in ws[1]:
            cell.font = Font(bold=True)

        for inv in invoices:

            ws.append([
                inv.source_file,
                inv.supplier,
                inv.vat_number,
                inv.invoice_number,
                inv.invoice_date,
                inv.subtotal,
                inv.vat_amount,
                inv.total,
            ])

        for column_cells in ws.columns:
            length = max(len(str(cell.value or "")) for cell in column_cells)
            ws.column_dimensions[column_cells[0].column_letter].width = min(length + 4, 40)

        wb.save(output_file)