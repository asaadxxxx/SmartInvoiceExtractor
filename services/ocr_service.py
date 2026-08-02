from core.ocr_engine import OCREngine


class OCRService:

    def __init__(self):
        self.engine = OCREngine()

    def extract_text(self, file_path):
        return self.engine.extract_text(file_path)