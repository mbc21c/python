from selenium.webdriver.common.keys import Keys
from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('http://cafe.naver.com/joonggonara')

    elem = driver.find_element_by_id('topLayerQueryInput')
    elem.send_keys('자전거')
    elem.send_keys(Keys.RETURN)
    
    iframe = driver.find_element_by_id('cafe_main')
    driver.switch_to_frame(iframe)

    form = driver.find_element_by_name('ArticleList')
    rows = form.find_elements_by_xpath('./table/tbody/tr')
    for row in rows:
        if row.get_attribute('align') != 'center':
            continue
        # 내용이 있는 tr태그
        elem = row.find_element_by_xpath('./td/span/span/a')
        print(elem.text)

except Exception as e:
    print(e)
finally:
    driver.quit()
