import requests
from bs4 import BeautifulSoup
import time

url = "https://news.hada.io/"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    tds = soup.select("td.topictitle > a")
    print(tds)
    for td in tds:
        title = td.text
        link = td.attrs["href"]
        print(title)
        print(link)
        print()
        time.sleep(0.2)
