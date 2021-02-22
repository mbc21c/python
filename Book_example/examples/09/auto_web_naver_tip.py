from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('https://naver.com')
    keyword = input('검색어를 입력하세요:' )

    elem = driver.find_element_by_id('query')
    elem.send_keys(keyword)
    elem.send_keys(Keys.RETURN)

    div = driver.find_element_by_class_name('_blogBase')
    #elem = div.find_element_by_tag_name('ul')
    blogs = div.find_elements_by_xpath('./ul/li')
    
    for blog in blogs:
        title_tag = blog.find_element_by_class_name('sh_blog_title')
        title = title_tag.get_attribute('title')
        if not title:
            title = title_tag.text
        print(title)
        link = title_tag.get_attribute('href')
        #print(link)

except Exception as e:
    print(e)
finally:
    driver.quit()
