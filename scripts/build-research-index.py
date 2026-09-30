from pathlib import Path
from html.parser import HTMLParser
import json
import re
from datetime import datetime

ROOT = Path(__file__).resolve().parents[1]
RESEARCH = ROOT / "research"
OUTPUT = RESEARCH / "index.json"

class MetaParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.title = ""
        self.meta = {}
        self.in_title = False
    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag == "meta" and attrs.get("name"):
            self.meta[attrs["name"].lower()] = attrs.get("content", "")
    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
    def handle_data(self, data):
        if self.in_title:
            self.title += data

reports = []
for path in RESEARCH.rglob("*.html"):
    if path.name.startswith("_") or path.name.upper() == "REPORT-TEMPLATE.HTML":
        continue

    parser = MetaParser()
    parser.feed(path.read_text(encoding="utf-8", errors="ignore"))

    rel = path.relative_to(RESEARCH).as_posix()
    title = parser.title.strip() or path.stem.replace("-", " ").replace("_", " ").title()
    description = parser.meta.get("description", "IY SECURITY research report.")
    category = parser.meta.get("iy-category", "Research")
    analysis_type = parser.meta.get("iy-type", "Analysis")
    tags = [x.strip() for x in parser.meta.get("iy-tags", "").split(",") if x.strip()]

    # Optional explicit date in YYYY-MM-DD format; otherwise use git/file date later if needed.
    date = parser.meta.get("iy-date", "")
    reports.append({
        "title": title,
        "description": description,
        "category": category,
        "type": analysis_type,
        "tags": tags,
        "date": date,
        "path": rel
    })

reports.sort(key=lambda x: (x["date"], x["title"]), reverse=True)
OUTPUT.write_text(json.dumps(reports, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
print(f"Generated {OUTPUT} with {len(reports)} reports.")
