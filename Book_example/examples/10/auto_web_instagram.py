from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome('chromedriver')

try:
    driver.get('https://www.instagram.com')

    btn = driver.find_element_by_link_text('로그인')
    btn.click()

    elem = driver.find_element_by_name('username')
    elem.send_keys('alghost.lee@gmail.com')

    elem = driver.find_element_by_name('password')
    elem.send_keys(open('password').read().strip())
    elem.send_keys(Keys.RETURN)

    time.sleep(3)

    elem = driver.find_element_by_class_name('_eduze')
    action = ActionChains(driver)
    action.move_to_element(elem)
    action.click()
    action.send_keys('#파이썬')
    action.perform()

    time.sleep(2)

    action.reset_actions()
    action.move_by_offset(0, 50)
    action.click()
    action.perform()

    time.sleep(5)

    elems = driver.find_elements_by_class_name('_havey')
    elem = elems[0]

    posts = elem.find_elements_by_class_name('_si7dy')
    action = ActionChains(driver)
    for post in posts:
        action.reset_actions()
        action.move_to_element(post)
        action.click()
        action.perform()

        time.sleep(1)

        try:
            elem = driver.find_element_by_link_text('좋아요')
            elem.click()
        except:
            pass

        action.reset_actions()
        action.send_keys(Keys.ESCAPE)
        action.perform()

        time.sleep(1)
except Exception as e:
    print(e)
finally:
    driver.quit()
