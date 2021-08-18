import requests
from bs4 import BeautifulSoup

html = requests.get("https://www.naver.com")

bsObject = BeautifulSoup(html, "html.parser")


print(bsObject)