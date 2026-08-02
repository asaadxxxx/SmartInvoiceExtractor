from PySide6.QtCore import QObject, Signal

from services.ocr_service import OCRService
from core.parser import InvoiceParser


class OCRWorker(QObject):

    progress = Signal(int)
    log = Signal(str)
    finished = Signal(list)

    def __init__(self, files):
        super().__init__()

        self.files = files

        self.ocr = OCRService()

        self.parser = InvoiceParser()

    def run(self):

        results = []

        total = len(self.files)

        for index, invoice_file in enumerate(self.files):

            try:

                self.log.emit(
                    f"قراءة {invoice_file.name}"
                )

                text = self.ocr.extract_text(
                    str(invoice_file.path)
                )

                invoice = self.parser.parse(text)

                invoice.source_file = invoice_file.name

                results.append(invoice)

            except Exception as e:

                self.log.emit(str(e))

            percent = int(
                ((index + 1) / total) * 100
            )

            self.progress.emit(percent)

        self.finished.emit(results)