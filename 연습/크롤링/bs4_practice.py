## 네이버 검색후 엑셀저장

import requests
from bs4 import BeautifulSoup
from openpyxl import Workbook

url = "https://kin.naver.com/search/list.nhn?query=%ED%8C%8C%EC%9D%B4%EC%8D%AC"

response = requests.get(url)

if response.status_code == 200:
    html = response.text
    soup = BeautifulSoup(html, "html.parser")
    ul = soup.select_one("ul.basic1")
    titles = ul.select("li > dl > dt > a")
    datas = []

    for title in titles:
        datas.append([title.get_text()])

    write_wb = Workbook()
    write_ws = write_wb.create_sheet("결과")

    for data in datas:
        print(data)
        write_ws.append(data)

    write_wb.save("d:/a.xlsx")
else:
    print(response.status_code)
