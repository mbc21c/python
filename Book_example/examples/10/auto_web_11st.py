from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome('chromedriver')

try:
    driver.get('http://11st.co.kr')

    elem = driver.find_element_by_id('AKCKwd')
    elem.send_keys('자전거')
    elem.send_keys(Keys.RETURN)

    from openpyxl import Workbook
    result_xlsx = Workbook()
    worksheet = result_xlsx.active
    worksheet.append(['판매자 이름', '상품명', '가격'])

    elems = driver.find_elements_by_xpath("//li[contains(@id, 'thisClick_')]")
    for elem in elems:
        title_tag = elem.find_element_by_class_name('info_tit')
        # print(title_tag.text)
        mall_tag = elem.find_element_by_class_name('benefit_tit')
        price_tag = elem.find_element_by_class_name('sale_price')
        print(mall_tag.text, title_tag.text, price_tag.text)
        worksheet.append([mall_tag.text, title_tag.text, price_tag.text])

    file_name = 'C:\\python\\examples\\2.6\\11st_result.xlsx'
    result_xlsx.save(file_name)

    from my_email import send_mail
    send_mail('이태화', 'alghost.lee@gmail.com', '테스트', file_name)
except Exception as e:
    print(e)
finally:
    driver.quit()
