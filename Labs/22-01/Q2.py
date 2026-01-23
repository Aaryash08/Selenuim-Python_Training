import requests
from bs4 import BeautifulSoup
import json

url = "https://aaryash08.github.io/Local-Restaurant-Project/"
response = requests.get(url)

if response.status_code != 200:
    print("Failed to fetch webpage")
    exit()

html_content = response.text

soup = BeautifulSoup(html_content, "lxml")

page_title = soup.title.string if soup.title else "No Title Found"

links = []
for link in soup.find_all("a"):
    href = link.get("href")
    if href:
        links.append(href)

table_data = []
table = soup.find("table")

if table:
    for row in table.find_all("tr"):
        cells = [cell.get_text(strip=True) for cell in row.find_all(["th", "td"])]
        if cells:
            table_data.append(cells)

extracted_data = {
    "title": page_title,
    "hyperlinks": links,
    "table_data": table_data
}
with open("extracted_data.json", "w", encoding="utf-8") as file:
    json.dump(extracted_data, file, indent=4)

print("Data extracted and saved to extracted_data.json")
