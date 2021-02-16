from selenium import webdriver
from datetime import datetime, timedelta
from my_email import send_mail

today = datetime.now()
diff = timedelta(days=7)
base_date = today - diff
base_date = datetime(base_date.year,base_date.month,base_date.day)
cron_base = '/Users/Alghost/Downloads'
opts = webdriver.ChromeOptions()
opts.add_argument('headless')
opts.add_argument('window-size=1920,1080')
driver = webdriver.Chrome(cron_base+'/chromedriver',chrome_options=opts)

try:
    keywords = open(cron_base+'/keywords.txt', 'r').readlines()
    matches = []

    driver.get('http://www.msit.go.kr/web/msipContents/contents.do?mId=MTE5')

    elems = driver.find_elements_by_xpath("//div[contains(@class,board-item)]/table/tbody/tr")
    for elem in elems:
        title_tag = elem.find_element_by_class_name('title')
        date_tag = elem.find_element_by_class_name('date')
        s_date = date_tag.text
        notice_date = datetime(int('20'+s_date[3:5]), int(s_date[-2:]), int(s_date[:2]))
        if notice_date > base_date:
            for k in keywords:
                if k.strip() in title_tag.text:
                    matches.append('%s: %s'%(str(notice_date)[:-9], title_tag.text))
                    break

    if matches:
        contents = '최근 올라온 공고가 있습니다.\n\n'

        contents += '\n'.join(matches)
        send_mail('이태화', 'alghost.lee@gmail.com', contents)

except Exception as e:
    print(e)
finally:
    driver.quit()
