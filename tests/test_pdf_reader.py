from core.pdf_reader import PDFReader

reader = PDFReader()

pdf = input("PDF Path: ")

print(reader.has_text(pdf))

print(reader.extract_text(pdf)[:1000])