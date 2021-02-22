from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('http://news.naver.com')

    elem = driver.find_elements_by_id('right.ranking_contents')

    news_list = elem.find_elements_by_tag_name('li')
    for news in news_list:
        print(news.text)

except Exception as e:
    print(e)
finally:
    driver.quit()
