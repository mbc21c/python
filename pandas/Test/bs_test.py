from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

search_word = input("검색어를 입력하세요 : ")
url = (
    "https://www.google.com/search?q="
    + quote_plus(search_word)
    + "&sxsrf=ACYBGNSPe8bZXL4LhwCck21hEs1ACF5NHg:1574219111921&source=lnms&tbm=nws&sa=X&ved=2ahUKEwiTs9uX5_flAhXW7GEKHYvjAZMQ_AUoA3oECA4QBQ&biw=1676&bih=781"
)

driver = webdriver.Chrome("D:\Source\python\pandas\Test\chromedriver.exe")
driver.get(url)
html = driver.page_source

soup = BeautifulSoup(html)

soup = soup.find_all(class_ = '.l.lLrAF')


for i in soup:
    print(i)
    print(i.a.attrs["href"])
    print()
"""     print(i.select_one(".ellip").text)
    print(i.select_one(".iUh30.bc").text)
    print(i.a.attrs["href"])
    print()
 """
driver.close()
