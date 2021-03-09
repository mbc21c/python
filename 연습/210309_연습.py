import requests
from bs4 import BeautifulSoup

webpage = requests.get("https://search.naver.com/search.naver?query=%ED%95%B4%EC%96%91%EA%B2%BD%EC%B0%B0&where=news&ie=utf8&sm=nws_hty")
soup = BeautifulSoup(webpage.content, "html.parser")

for x in range(0, 100):
    news_company = soup.select(".news_area .info_group>a")[x].get_text()
    news_title = soup.select("a.news_tit")[x].get_text()
    print(news_company)
    print(news_title)