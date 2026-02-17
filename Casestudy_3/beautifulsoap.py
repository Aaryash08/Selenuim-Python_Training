from bs4 import BeautifulSoup

# Read local HTML file
with open("patient.html", "r", encoding="utf-8") as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, "lxml")

rows = soup.find_all("tr")[1:]  # skip header row

print("Patient Details:\n")

for row in rows:
    cols = row.find_all("td")
    name = cols[0].text
    age = cols[1].text
    disease = cols[2].text
    doctor = cols[3].text

    print(f"Name: {name}, Age: {age}, Disease: {disease}, Doctor: {doctor}")
