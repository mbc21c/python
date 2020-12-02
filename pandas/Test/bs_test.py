from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

<<<<<<< HEAD
base_url = 'https://www.google.com/search?q='
search_word = quote_plus(input('검색할 단어를 입력하세요 : '))
url = base_url + search_word +'&sxsrf=ACYBGNT7DRw71m70BpgXOtjKvTRoAVxjtA:1574244938278&source=lnms&tbm=nws&sa=X&ved=2ahUKEwjji9eyx_jlAhWHBKYKHRiGD88Q_AUoA3oECA4QBQ&biw=1920&bih=916'

driver = webdriver.Chrome('J:\Source\python\pandas\Test\chromedriver.exe')
driver.get(url)

soup = BeautifulSoup(driver.page_source)

class_Text = soup.select("[class~=l.lLrA]")

for i in class_Text:
    print(i)
    print(i.find("a", "href"))
    print()
=======
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
>>>>>>> bb224da0197bae26686267323ad763813a80507c
