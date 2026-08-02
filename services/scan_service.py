from core.scanner import FileScanner


class ScanService:

    def __init__(self):
        self.scanner = FileScanner()

    def scan_folder(self, folder):
        return self.scanner.scan(folder)