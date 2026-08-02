import json

from core.row_parser import RowParser

with open("sample.json", "r", encoding="utf-8") as f:
    words = json.load(f)

parser = RowParser(words)

parser.print_rows()