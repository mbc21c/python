import requests
from bs4 import BeautifulSoup
import time

url = "https://bbs.ruliweb.com/market/board/1020"

response = requests.get(url)
if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    titles = soup.select("div > a.deco")

    for title in titles:
        print(title.text)
        link = title.attrs["href"]
        print(link)
        print()
