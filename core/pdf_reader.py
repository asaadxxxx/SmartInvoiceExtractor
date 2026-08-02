import fitz
from PIL import Image
import io


class PDFReader:

    def extract_text(self, pdf_path: str) -> str:
        doc = fitz.open(pdf_path)

        text = []

        for page in doc:
            page_text = page.get_text().strip()

            if page_text:
                text.append(page_text)

        doc.close()

        return "\n".join(text)

    def has_text(self, pdf_path: str) -> bool:
        return len(self.extract_text(pdf_path).strip()) > 20

    def pdf_to_images(self, pdf_path: str):

        doc = fitz.open(pdf_path)

        images = []

        for page in doc:

            pix = page.get_pixmap(dpi=300)

            img = Image.open(
                io.BytesIO(
                    pix.tobytes("png")
                )
            )

            images.append(img)

        doc.close()

        return images