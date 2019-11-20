from urllib.parse import quote_plus
from bs4 import BeautifulSoup
from selenium import webdriver

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