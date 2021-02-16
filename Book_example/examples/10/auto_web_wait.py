﻿from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


driver = webdriver.Chrome('chromedriver')

try:
    driver.get('https://www.instagram.com')

    wait = WebDriverWait(driver, 60)

    cond = EC.element_to_be_clickable((By.LINK_TEXT, '로그인'))
    btn = wait.until(cond)
    btn.click()

    input()

except Exception as e:
    print(e)
finally:
    driver.quit()
