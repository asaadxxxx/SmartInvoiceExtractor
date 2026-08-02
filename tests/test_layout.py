import json

from core.layout_analyzer import LayoutAnalyzer

with open("sample.json", "r", encoding="utf-8") as f:
    words = json.load(f)

layout = LayoutAnalyzer(words)

rows = layout.build_lines()

for row in rows:

    print("=" * 80)

    print(" | ".join(
        w["text"] for w in row
    ))