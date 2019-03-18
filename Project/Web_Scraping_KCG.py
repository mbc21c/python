from bs4 import BeautifulSoup
import requests

def get_html(url):
   _html = ""
   resp = requests.get(url)
   print(resp)
   if resp.status_code == 200:
      _html = resp.text
   return _html

URL = "https://search.naver.com/search.naver?&where=news&query=%ED%95%B4%EC%96%91%EA%B2%BD%EC%B0%B0&sm=tab_tmr&frm=mr&nso=so:r,p:all,a:all&sort=0"
html = get_html(URL)

print("{}".format(html))

soup = BeautifulSoup(html, 'html.parser')

