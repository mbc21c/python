# from openpyxl import Workbook
# from bs4 import BeautifulSoup
# from selenium import webdriver
# import os

# path = os.path.dirname(os.path.realpath(__file__)) + "/chromedriver"
# driver = webdriver.Chrome(path)

# url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=제주해경"
# # url

# driver.get(url)
# req = driver.page_source
# print(req)
# soup = BeautifulSoup(req, 'html.parser')

# articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')
# # 코드 검사 > copy select (안에 가져올 코드가 어떤 것인지 확인) > ul 안에 > li 코드 가져와서 저장

# wb = Workbook()
# ws1 = wb.active
# ws1.title = "articles"
# # 엑셀 파일 이름
# ws1.append(["제목", "링크", "신문사"])
# #  엑셀 1번째 가로 줄에 append

# for article in articles:
#     title = article.select_one('dl > dt > a').text
#     # article 에서 dl > dt > a 의 text 만 저장
#     url =  article.select_one('dl > dt > a')['href']
#     # article 에서 dl > dt > a 에서 href 만 저장 (title)
#     comp = article.select_one('span._sp_each_source').text.split(' ')[0].replace('언론사' , '')
#     # article 에서 언론사 copy select 하여 text 만 저장 후 split (' ' 공백으로 자르기) 후 [0] 처음것만 가져오기
#     # replace '언론사' 는 '' 공백으로 표시

#     ws1.append([title, url, comp])
#     # 엑셀에 첫번째 가로줄에 append

# driver.quit()
# wb.save(filename='articles.xlsx')
# # 엑셀에 저장하기


from bs4 import BeautifulSoup
from selenium import webdriver
import os

path = os.path.dirname(os.path.realpath(__file__)) + "/chromedriver"
driver = webdriver.Chrome(path)

driver = webdriver.Chrome(path)

url = "https://search.naver.com/search.naver?where=news&sm=tab_jum&query=추석"

driver.get(url)
req = driver.page_source
soup = BeautifulSoup(req, 'html.parser')

articles = soup.select('#main_pack > div.news.mynews.section._prs_nws > ul > li')

for article in articles:
    a_tag = article.select_one('dl > dt > a')

    title = a_tag.text
    url = a_tag['href']
    comp = article.select_one('span._sp_each_source').text.slpit(' ')[0]
    print(title, url, comp)

driver.quit()