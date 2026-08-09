from pathlib import Path
from bs4 import BeautifulSoup

html_file = Path("data/raw/abgruendiges-wappnen.html")

with html_file.open("r", encoding="utf-8") as file:
    html = file.read()

soup = BeautifulSoup(html, "html.parser")

print(soup.get_text(" ", strip=True))
