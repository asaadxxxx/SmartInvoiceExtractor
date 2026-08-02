from dataclasses import dataclass


@dataclass
class InvoiceFile:

    path: str
    extension: str
    pages: int = 1

    def is_pdf(self):

        return self.extension.lower() == ".pdf"

    def is_image(self):

        return self.extension.lower() in [
            ".jpg",
            ".jpeg",
            ".png",
            ".bmp",
            ".tif",
            ".tiff",
        ]