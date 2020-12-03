# -*- coding: utf-8 -*-
# write.py
from selenium import webdriver
import time
import configparser
 
Config = configparser.ConfigParser()
 
#config 파일 로드
Config.read('./info.conf', "utf-8")
id = Config.get('clien', 'id')
pw = Config.get('clien', 'pw')
title = Config.get('clien', 'title')
content = Config.get('clien', 'content')
chromedriver = Config.get('clien', 'chromedriver')
agent = Config.get('clien', 'agent')
t_board = Config.get('clien', 't_board')
repeat = Config.get('clien', 'repeat')
repeat = int(repeat)
interval = Config.get('clien', 'interval')
 
 
URL = 'https://www.clien.net/service/CLIEN'
options = webdriver.ChromeOptions()
 
print("   ################################################")
print("")
print("    클리앙 자동 글쓰기 프로그램을 시작합니다.")
print("    ")
print("    사용법")
print("    contents는 태그제외 3자 이상 입력해야 합니다. (html 사용가능)")
print("")
print("   ################################################")
 
#headless 모드
options.add_argument('headless')
options.add_argument('window-size=1920x1080')
options.add_argument("disable-gpu")
options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
 
 
 
 
 
#user-agent 변경
options.add_argument(agent)
 
#크롬 드라이버 로드
driver = webdriver.Chrome(chromedriver, options=options)
driver.implicitly_wait(3)
 
#메인 페이지 로드
driver.get(URL)
# plugins 탐지 우회
driver.execute_script("Object.defineProperty(navigator, 'plugins', {get: function() {return[1, 2, 3, 4, 5]}})")
# lanuages 탐지 우회
driver.execute_script("Object.defineProperty(navigator, 'languages', {get: function() {return ['ko-KR', 'ko']}})")
# gpu 탐지 우회
driver.execute_script("const getParameter = WebGLRenderingContext.getParameter;WebGLRenderingContext.prototype.getParameter = function(parameter) {if (parameter === 37445) {return 'NVIDIA Corporation'} if (parameter === 37446) {return 'NVIDIA GeForce GTX 980 Ti OpenGL Engine';}return getParameter(parameter);};")
 
 
time.sleep(3)
 
#로그인 구간
driver.find_element_by_name('userId').send_keys(id)
driver.find_element_by_name('userPassword').send_keys(pw)
driver.find_element_by_name('로그인하기').click()
 
print("")
print("   로그인에 성공하였습니다. ")
print("   글쓰기 페이지로 이동합니다.")
 
 
for i in range(0, repeat):
 
    # 글작성 페이지 로드
    driver.get(t_board)
    time.sleep(3)
 
    #글작성 구간
    driver.find_element_by_class_name('input_title').send_keys(title)
    driver.find_element_by_class_name("fr-element").send_keys(content)
    driver.find_element_by_class_name("button-agree").click()
    print(f'     {repeat}중 {i}회가 시행되었습니다.')
    time.sleep(int(interval))
 
print(f"     {title}란 제목의 글쓰기가 총 {repeat}회 성공하였습니다. 5초후 종료합니다.")
time.sleep(5)
driver.quit()