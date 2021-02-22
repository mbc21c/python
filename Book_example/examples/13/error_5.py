from selenium import webdriver

driver = webdriver.Chrome('./chromedriver')

try:
    driver.get('http://naver.com')

    elem = driver.find_element_by_class_name('query')

except Exception as e:
    print(e)
finally:
    driver.quit()
