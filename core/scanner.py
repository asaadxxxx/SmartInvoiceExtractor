from pathlib import Path
from models.invoice_file import InvoiceFile

SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".jpg",
    ".jpeg",
    ".png",
    ".tif",
    ".tiff",
    ".zip"
}


class FileScanner:

    def scan(self, folder: str):

        files = []

        root = Path(folder)

        if not root.exists():
            raise FileNotFoundError(folder)

        for file in root.rglob("*"):

            if file.is_file() and file.suffix.lower() in SUPPORTED_EXTENSIONS:
                files.append(InvoiceFile(file))

        files.sort(key=lambda x: x.name.lower())

        return files