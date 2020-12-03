import pickle
from pandas import Series, DataFrame
import locale
import time

#.stock 파일 불러와서 html 파일 생성 /20-09-01
def CalMF(fileDate):
    code = []
    per = []
    roa = []

    with open(fileDate + '.stock','rb') as f:
        stock = pickle.load(f)

    for cd in stock:
        if len(stock[cd]) < 5: #PER나 ROA가 없는 기업 제외
            continue

        try:
            if int(stock[cd][5]) < 1000: #시가총액이 1000억 이하인 기업 제외
                continue

            if stock[cd][3] <= 0: #PER가 -인 기업 제외
                continue
                
            # 기업부채가 50%가 넘어가는 회사 제외

            
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
    'PER(순위)':col_per_rank, 'ROA(순위)':col_roa_rank,
    '업종':col_field, '순위합산':col_sum}

    result = DataFrame(raw_data, 
    columns=['종목명','종목코드','주가','PER(순위)','ROA(순위)','업종','순위합산'], 
    index=row_mf_rank)
        
    return (result, stock)    

if __name__ == "__main__":
    
    now = time.localtime()
    fileName_stock = ('%04d-%02d-%02d.stock' % (now.tm_year, now.tm_mon, now.tm_mday))
    fileName_html = ('%04d-%02d-%02d.html' % (now.tm_year, now.tm_mon, now.tm_mday))

    # 종목코드를 구한다.
    result,newstock = CalMF("2020-09-02")

    result.iloc[1:100].to_html(fileName_html)