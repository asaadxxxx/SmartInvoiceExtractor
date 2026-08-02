from paddleocr import PaddleOCR


class OCREngine:

    def __init__(self):
        self.ocr = PaddleOCR(lang="ar")

    def extract_text(self, image_path):

        result = self.ocr.predict(image_path)

        lines = []

        for page in result:

            if "rec_texts" in page:

                lines.extend(page["rec_texts"])

        return "\n".join(lines)