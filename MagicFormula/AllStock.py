# -*- coding: utf-8 -*-
"""
Created on Wed Jun 15 11:26:02 2016

@author: 리밸런서 (cafe.naver.com/rebalancer)
"""

import requests            # 웹페이지 호출
from bs4 import BeautifulSoup        # 웹페이지 파싱
import re                            # 정규식
import datetime                          # 시간 딜레이
import time
import pickle                        # 자료형 저장
from pandas import Series, DataFrame
import locale

# Daum 전종목 시세 페이지를 파싱해 전종목코드와 업종 시세, 재무정보를 읽어 파일로 저장한다.

# 파싱한 정보를 저장할 전역 변수
# 종목코드로 종목코드에 해당하는 정보를 찾을 수 있게 Dictionary 형태로 구성
stock = {}  # {종목코드:[종목명,시장구분,업종,현 재가,PER,재무정보,추정실적 컨센서스]}

def GetStockCode():
    url = 'https://www.sedaily.com/Stock/Quote?type=1'
    
    try:
        f = requests.get(url)
    except requests.exceptions.RequestException as e:
        # do something
        print(e + ' 10초 대기')
        time.sleep(10)
    else:
        soup = BeautifulSoup(f.text, 'lxml')
            
    
    # 'class'속성의 값이 'fl_le'인 'h4'태그를 모두 찾는다.
    fields = soup.find_all('div',{'class':'table'})
    
    for field in fields: # 검색된 모든 'h4' 태그에 대하여 for문 안의 작업을 수행
        dl=field.find('dl', {'class':'thead'})
        dt=dl.find('dt')
        fieldName=dt.text
        if fieldName == '금융': # 금융업은 제외 시킨다.
            continue
        
        # 'h4' 태그 다음에 있는 'table' 태그를 table 변수로 가져 온다.
        table=field.find_all('dl',{'class':'tbody'})
        # 'table' 내에서 'class'속성값이 'txt'인 'td'를 모두 찾는다.
        for dl in table: # 검색된 모든 'td'에 대하여 for문 안의 작업을 수행
            name = dl.find('dt').get_text()
            dd = dl.find('dd')
            code = dd.get('id').replace('dd_Item_','')
            price = dd.find('span').get_text().replace(',','')
            stock[code] = [name, fieldName, price]


# 종목의 PER를 가져온다.
# 에러 발생시 에러메시지를 리턴한다. 
def GetPER(code):

    url = 'https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A' + code + '&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=701'
    
    try:
        f = requests.get(url)
    except requests.exceptions.RequestException as e:
        # do something
        print(e + ' 10초 대기')
        time.sleep(10)
    else:
        soup = BeautifulSoup(f.text, 'lxml')
    
    fields = soup.find_all('tr')

    for tr in fields: 
        span = tr.find_all('span',{'class':'txt_acd'})
        for dt in span:
            dts = dt.text
            if dts == 'PER':
                per = tr.find_all('td', {'class':'r'})
                if len(per) != 3:
                    continue
                try:
                    for index,b in enumerate(per):
                        if index == 0:
                            stock[code].append(float(b.get_text().replace(',','')))
                            break
                except:
                    return '[' + code + '] PER 검출 실패'


def GetROA(code):

    url = 'https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A' + code + '&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=701'
    
    try:
        f = requests.get(url)
    except requests.exceptions.RequestException as e:
        # do something
        print(e + ' 10초 대기')
        time.sleep(10)
    else:
        soup = BeautifulSoup(f.text, 'lxml')
    
    fields = soup.find_all('tr')

    for tr in fields: 
        span = tr.find_all('span',{'class':'txt_acd'})
        for dt in span:
            dts = dt.text
            if dts == 'ROA':
                roa = tr.find_all('td', {'class':'r'})
                if len(roa) != 8:
                    continue
                try:
                    for index,b in enumerate(roa):
                        if index == 2:
                            stock[code].append(float(b.get_text().replace(',','')))
                            return
                except:
                    return '[' + code + '] ROA 검출 실패'

def GetCompanyCost(code):

    url = 'https://comp.fnguide.com/SVO2/ASP/SVD_Main.asp?pGB=1&gicode=A' + code + '&cID=&MenuYn=Y&ReportGB=&NewMenuID=11&stkGb=701'
    
    try:
        f = requests.get(url)
    except requests.exceptions.RequestException as e:
        # do something
        print(e + ' 10초 대기')
        time.sleep(10)
    else:
        soup = BeautifulSoup(f.text, 'lxml')
    
    fields = soup.find_all('table',{'class':'us_table_ty1 h_fix zigbg_no th_topbdno'})

    for field in fields: 
        tbodys = field.find_all('tbody')
        for tbody in tbodys:
            trs = tbody.find_all('tr')
            for tr in trs:
                divs = tr.find_all('div')
                for div in divs:
                    divText = div.text
                    if divText == "시가총액":
                        companycost = tr.find_all('td', {'class':'r'})
                        if len(companycost) != 3:
                            continue
                        try:
                            for index,b in enumerate(companycost):
                                if index == 0:
                                    stock[code].append(int(b.get_text().replace(',','')))
                                    return
                        except:
                            return '[' + code + '] 시가총액 검출 실패'

def CalMF():
    code = []
    per = []
    roa = []

    for cd in stock:
        if len(stock[cd]) < 5:
            continue

        try:
            if int(stock[cd][5]) < 1000:
                continue

            if stock[cd][3] <= 0:
                continue
                
            readPer = stock[cd][3]
            readRoa = stock[cd][4]

            code.append(cd)
            per.append(float(readPer))
            roa.append(float(readRoa))
        except:
            pass
    
    per_rank = Series(per, index=code).rank(method='min')
    roa_rank = Series(roa, index=code).rank(method='min', ascending=False)

    mf_rank = (per_rank + roa_rank).sort_values()

    col_name = []
    col_cd = []
    col_price = []
    col_per_rank = []
    col_roa_rank = []
    col_field = []
    col_sum = []

    row_mf_rank = []

    for index, cd in enumerate(mf_rank.index):
        row_mf_rank.append(index)

        col_name.append(stock[cd][0])
        col_cd.append(cd)
        col_price.append(stock[cd][2])
        col_per_rank.append(format('%.2f(%.0f)'%(stock[cd][3], per_rank[cd])))
        col_roa_rank.append(format('%.2f(%.0f)'%(stock[cd][4], roa_rank[cd])))
        col_field.append(stock[cd][1])
        col_sum.append(int(mf_rank[cd]))

    raw_data = {'종목명':col_name, '종목코드':col_cd, '주가':col_price,
    'PER(순위)':col_per_rank, 'ROA(순위)':col_roa_rank, '업종':col_field, '순위합산':col_sum}

    result = DataFrame(raw_data, 
    columns=['종목명','종목코드','주가','PER(순위)','ROA(순위)','업종','순위합산'], 
    index=row_mf_rank)
        
    return (result, stock)    

if __name__ == "__main__":
    
    now = time.localtime()
    fileName_stock = ('%04d-%02d-%02d.stock' % (now.tm_year, now.tm_mon, now.tm_mday))
    fileName_html = ('%04d-%02d-%02d.html' % (now.tm_year, now.tm_mon, now.tm_mday))

    # 종목코드를 구한다.
    GetStockCode()    # 코스피 
    for index, code in enumerate(stock):
        retMsg = GetPER(code)
        retMsg = GetROA(code)
        retMsg = GetCompanyCost(code)

        print(index+1, '/', len(stock), ' ', code)
        time.sleep(0.1)

    #.stock 파일 생성
    with open(fileName_stock,'wb') as f:
        pickle.dump(stock, f)

    """ 
    # 파싱 된 정보를 파일로 저장한다.
    with open(fileName,'wb') as f:
        pickle.dump(stock, f)


    다시 읽어올 때는 요렇게 하면 된다.
    with open('2016-06-17.stock', 'rb') as f:
        stock = pickle.load(f)

    #20-09-01 추가 : html파일로 바로 생성
    result,newstock = CalMF()

    result.iloc[1:100].to_html(fileName_html)
    """
        