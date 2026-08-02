from core.pdf_reader import PDFReader
from core.ocr_engine import OCREngine
from core.invoice_extractor import InvoiceExtractor


class ExtractionService:

    def __init__(self):

        self.pdf = PDFReader()
        self.ocr = OCREngine()

    def extract(self, file_path):

        extractor = InvoiceExtractor()

        return extractor.extract(file_path)