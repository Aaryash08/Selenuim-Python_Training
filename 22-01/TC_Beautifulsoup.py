import requests
from bs4 import BeautifulSoup
import json

from Labs.Day8.Q2 import extracted_data

url = "https://aaryash08.github.io/Local-Restaurant-Project/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'lxml')
pagetitle=soup.title.string if soup.title.string else "No title"
print(pagetitle)

for link in soup.find_all('a'):
    href=link.get('href')
    print(href)
tabledata=[]
table = soup.find("table")
if table:
    rows=table.find_all('tr')
    for row in rows[1:]:
        cols=row.find_all('td')
        row_data=[col.text.strip() for col in cols]
        print(row_data)
        tabledata.append(row_data)
extracted_data={
    "page_title":pagetitle,
    "total_links":len(href),
    "links":href,
    "table_data":tabledata
}

with open('extracted_data.json', 'w',encoding="utf-8") as file:
    json.dump(extracted_data, file,indent=4)