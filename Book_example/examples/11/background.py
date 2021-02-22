from selenium import webdriver

opts = webdriver.ChromeOptions()
opts.add_argument('headless')
opts.add_argument('window-size=1920,1080')

driver = webdriver.Chrome('/Users/Alghost/Downloads/chromedriver',chrome_options=opts)

try:
    driver.get('http://naver.com')
    print(driver.title)
except Exception as e:
    print(e)
finally:
    driver.quit()
