from selenium import webdriver
from bs4 import BeautifulSoup as bs

import time
import os, sys

path = "D:/Source/python/pandas/Naver_Crolling_selenium/chromedriver.exe"
driver = webdriver.Chrome(path)

driver.get('https://nid.naver.com/nidlogin.login')

id = 'mbc_21c'
pw = 'qordhrgml1114'

driver.execute_script("document.getElementsByName('id')[0].value=\'" + id + "\'")
driver.execute_script("document.getElementsByName('pw')[0].value=\'" + pw + "\'")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

cafe_url = 'https://cafe.naver.com/xst'
url = '/ArticleList.nhn?search.clubid=27738104&search.menuid=502&search.boardtype=L'

soup = bs(driver.page_source, 'html.parser')

print(soup)

driver.get(cafe_url + url)




time.sleep(30)

driver.close()

