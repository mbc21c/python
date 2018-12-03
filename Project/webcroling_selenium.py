from selenium import webdriver

driver = webdriver.Chrome('c:/chromedriver/chromedriver')
driver.implicitly_wait(3)
# url에 접근한다.
driver.get('https://search.naver.com/search.naver?&where=news&query=%ED%95%B4%EC%96%91%EA%B2%BD%EC%B0%B0&sort=1&sm=tab_smr&nso=so:dd,p:all,a:all')
#driver.get('https://nid.naver.com/nidlogin.login')

#driver.find_element_by_name("id").send_keys("mbc_21c")
#driver.find_element_by_name("pw").send_keys("qordhrgml1114")

#driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()