from dataclasses import dataclass
from pathlib import Path


@dataclass
class InvoiceFile:
    path: Path

    @property
    def name(self):
        return self.path.name

    @property
    def extension(self):
        return self.path.suffix.upper().replace(".", "")

    @property
    def size_kb(self):
        return round(self.path.stat().st_size / 1024, 2)

    @property
    def folder(self):
        return str(self.path.parent)

    @property
    def status(self):
        return "جاهز"