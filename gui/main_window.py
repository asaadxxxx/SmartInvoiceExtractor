from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QHBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
    QMessageBox,
    QTableWidget,
    QTableWidgetItem,
    QProgressBar,
    QPlainTextEdit,
)

from services.scan_service import ScanService


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Invoice Extractor PRO")
        self.resize(1200, 700)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()

        title = QLabel("Smart Invoice Extractor PRO")
        title.setStyleSheet("font-size:22px;font-weight:bold;")

        self.btn_folder = QPushButton("📂 اختيار مجلد الفواتير")
        self.btn_zip = QPushButton("📦 اختيار ملف ZIP")
        self.btn_start = QPushButton("▶ بدء استخراج البيانات")

        self.btn_folder.clicked.connect(self.open_folder)
        self.btn_zip.clicked.connect(self.open_zip)

        buttons = QHBoxLayout()
        buttons.addWidget(self.btn_folder)
        buttons.addWidget(self.btn_zip)
        buttons.addWidget(self.btn_start)

        self.lbl_count = QLabel("عدد الملفات : 0")

        self.table = QTableWidget()
        self.table.setColumnCount(5)
        self.table.setHorizontalHeaderLabels([
            "اسم الملف",
            "النوع",
            "الحجم KB",
            "المجلد",
            "الحالة"
        ])

        self.progress = QProgressBar()
        self.progress.setValue(0)

        self.log = QPlainTextEdit()
        self.log.setReadOnly(True)
        self.log.setMaximumHeight(120)

        layout.addWidget(title)
        layout.addLayout(buttons)
        layout.addWidget(self.lbl_count)
        layout.addWidget(self.table)
        layout.addWidget(self.progress)
        layout.addWidget(self.log)

        central.setLayout(layout)

    def open_folder(self):

        folder = QFileDialog.getExistingDirectory(
            self,
            "اختر مجلد الفواتير"
        )

        if not folder:
            return

        try:

            service = ScanService()

            files = service.scan_folder(folder)

            self.table.setRowCount(0)

            for invoice in files:

                row = self.table.rowCount()

                self.table.insertRow(row)

                self.table.setItem(row, 0, QTableWidgetItem(invoice.name))
                self.table.setItem(row, 1, QTableWidgetItem(invoice.extension))
                self.table.setItem(row, 2, QTableWidgetItem(str(invoice.size_kb)))
                self.table.setItem(row, 3, QTableWidgetItem(invoice.folder))
                self.table.setItem(row, 4, QTableWidgetItem(invoice.status))

            self.lbl_count.setText(f"عدد الملفات : {len(files)}")

            self.progress.setValue(100)

            self.log.appendPlainText(
                f"تم العثور على {len(files)} ملف."
            )

        except Exception as e:

            QMessageBox.critical(
                self,
                "خطأ",
                str(e)
            )

    def open_zip(self):

        QFileDialog.getOpenFileName(
            self,
            "اختر ملف ZIP",
            "",
            "ZIP Files (*.zip)"
        )