from paddleocr import PaddleOCR


class OCREngine:

    def __init__(self):
        self.ocr = PaddleOCR(
            use_angle_cls=False,
            lang="ar"
        )

    def read(self, image_path):

        result = self.ocr.ocr(image_path, cls=False)

        words = []

        if result and result[0]:

            for item in result[0]:

                box = item[0]
                text = item[1][0]
                score = float(item[1][1])

                words.append({
                    "text": text,
                    "box": box,
                    "confidence": score
                })

        return words