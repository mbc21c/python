from selenium import webdriver

driver = webdriver.Chrome('chromedriver')

try:
    driver.get('https://www.quirksmode.org/js/popup.html#create')

    btn = driver.find_element_by_link_text("Open popup")
    btn.click()

    wins = driver.window_handles
    driver.switch_to_window(wins[1])

    print(driver.title)

    input()

except Exception as e:
    print(e)
finally:
    driver.quit()
