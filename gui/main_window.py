from PySide6.QtWidgets import (
    QMainWindow,
    QWidget,
    QVBoxLayout,
    QPushButton,
    QLabel,
    QFileDialog,
)


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Invoice Extractor")
        self.resize(900, 600)

        central = QWidget()
        self.setCentralWidget(central)

        layout = QVBoxLayout()

        title = QLabel("Smart Invoice Extractor")
        title.setStyleSheet("font-size:22px;font-weight:bold;")

        self.btn_folder = QPushButton("اختيار مجلد الفواتير")
        self.btn_zip = QPushButton("اختيار ملف ZIP")
        self.btn_start = QPushButton("بدء استخراج البيانات")

        self.btn_folder.clicked.connect(self.open_folder)
        self.btn_zip.clicked.connect(self.open_zip)

        layout.addWidget(title)
        layout.addWidget(self.btn_folder)
        layout.addWidget(self.btn_zip)
        layout.addWidget(self.btn_start)

        central.setLayout(layout)

    def open_folder(self):
        QFileDialog.getExistingDirectory(self, "اختر مجلد الفواتير")

    def open_zip(self):
        QFileDialog.getOpenFileName(
            self,
            "اختر ملف ZIP",
            "",
            "ZIP Files (*.zip)"
        )