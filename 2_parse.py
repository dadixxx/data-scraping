import requests
from bs4 import BeautifulSoup


url = "https://fr.wikipedia.org/wiki/Alger"
resp = requests.get(url)
soup = BeautifulSoup(resp.text, "html.parser")

trs = soup.find_all("tr")
for tr in trs:
    th = tr.find("th")
    td = tr.find("td")
    if th:
        if th.text.strip() == "Population":
            print(td.text.strip())
