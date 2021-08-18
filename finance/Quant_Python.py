import pandas as pd
import os
import time
import bs4
import requests


def make_fs_dataframe(firm_code):
    fs_url = (
        "https://comp.fnguide.com/SVO2/asp/SVD_Finance.asp?pGB=1&cID=&MenuYn=Y&ReportGB=D&NewMenuID=103&stkGb=701&gicode="
        + firm_code
    )
    fs_page = requests.get(fs_url)
    fs_tables = pd.read_html(fs_page.text)

    temp_df = fs_tables[0]
    temp_df = temp_df.set_index(temp_df.columns[0])
    temp_df = temp_df[temp_df.columns[:4]]
    temp_df = temp_df.loc[["매출액", "영업이익", "당기순이익"]]

    temp_df2 = fs_tables[2]
    temp_df2 = temp_df2.set_index(temp_df2.columns[0])
    temp_df2 = temp_df2.loc[["자산", "부채", "자본"]]

    temp_df3 = fs_tables[4]
    temp_df3 = temp_df3.set_index(temp_df3.columns[0])
    temp_df3 = temp_df3.loc[["영업활동으로인한현금흐름"]]

    fs_df = pd.concat([temp_df, temp_df2, temp_df3])

    return fs_df


def change_df(firm_code, dataframe):
    for num, col in enumerate(dataframe.columns):
        temp_df = pd.DataFrame({firm_code: dataframe[col]})
        temp_df = temp_df.T
        temp_df.columns = [[col] * len(dataframe), temp_df.columns]
        if num == 0:
            total_df = temp_df
        else:
            total_df = pd.merge(
                total_df, temp_df, how="outer", left_index=True, right_index=True
            )

    return total_df


def make_fr_dataframe(firm_code):
    fr_url = (
        "https://comp.fnguide.com/SVO2/asp/SVD_FinanceRatio.asp?pGB=1&cID=&MenuYn=Y&ReportGB=D&NewMenuID=104&stkGb=701&gicode="
        + firm_code
    )
    fr_page = requests.get(fr_url)
    fr_tables = pd.read_html(fr_page.text)

    temp_df = fr_tables[0]
    temp_df = temp_df.set_index(temp_df.columns[0])
    temp_df = temp_df.loc[
        [
            "유동비율(유동자산 / 유동부채) * 100 유동비율계산에 참여한 계정 펼치기",
            "부채비율(총부채 / 총자본) * 100 부채비율계산에 참여한 계정 펼치기",
            "영업이익률(영업이익 / 영업수익) * 100 영업이익률계산에 참여한 계정 펼치기",
            "ROA(당기순이익(연율화) / 총자산(평균)) * 100 ROA계산에 참여한 계정 펼치기",
            "ROIC(세후영업이익(연율화)/영업투하자본(평균))*100 ROIC계산에 참여한 계정 펼치기",
        ]
    ]
    temp_df.index = ["유동비율", "부채비율", "영업이익률", "ROA", "ROIC"]
    return temp_df


def make_invest_dataframe(firm_code):
    invest_url = (
        "https://comp.fnguide.com/SVO2/asp/SVD_Invest.asp?pGB=1&cID=&MenuYn=Y&ReportGB=D&NewMenuID=105&stkGb=701&gicode="
        + firm_code
    )
    invest_page = requests.get(invest_url)
    invest_tables = pd.read_html(invest_page.text)
    temp_df = invest_tables[1]

    temp_df = temp_df.set_index(temp_df.columns[0])
    temp_df = temp_df.loc[
        [
            "PER수정주가(보통주) / 수정EPS PER계산에 참여한 계정 펼치기",
            "PCR수정주가(보통주) / 수정CFPS PCR계산에 참여한 계정 펼치기",
            "PSR수정주가(보통주) / 수정SPS PSR계산에 참여한 계정 펼치기",
            "PBR수정주가(보통주) / 수정BPS PBR계산에 참여한 계정 펼치기",
            "총현금흐름세후영업이익 + 유무형자산상각비 총현금흐름",
        ]
    ]
    temp_df.index = ["PER", "PCR", "PSR", "PBR", "총현금흐름"]
    return temp_df


os.chdir(os.getcwd() + "/finance")

path = os.getcwd() + "\data_4440_20210530.xls"
print(path)
code_data = pd.read_excel(path)
code_data = code_data[["단축코드", "한글 종목명"]]

print(code_data)

for num, code in enumerate(code_data["단축코드"]):
    try:
        print(num, code)
        time.sleep(1)
        try:
            fs_df = make_fs_dataframe(code)
            fr_df = make_fr_dataframe(code)
        except requests.exceptions.Timeout:
            time.sleep(60)
            fs_df = make_fs_dataframe(code)
            fr_df = make_fr_dataframe(code)
        fs_df_changed = change_df(code, fs_df)
        fr_df_changed = change_df(code, fr_df)
        if num == 0:
            total_fs = fs_df_changed
            total_fr = fr_df_changed
        else:
            total_fs = pd.concat([total_fs, fs_df_changed])
            total_fr = pd.concat([total_fr, fr_df_changed])
    except ValueError:
        continue
    except KeyError:
        continue

total_fs.to_excel(os.getcwd() + "\재무제표데이터.xls")
total_fr.to_excel(os.getcwd() + "\재무비율데이터.xls")

for num, code in enumerate(code_data["단축코드"][313:]):
    try:
        print(num, code)
        time.sleep(1)
        try:
            invest_df = make_invest_dataframe(code)
        except requests.exceptions.Timeout:
            time.sleep(60)
            invest_df = make_invest_dataframe(code)
        invest_df_changed = change_df(code, invest_df)
        if num == 0:
            total_invest = invest_df_changed
        else:
            total_invest = pd.concat([total_invest, invest_df_changed])
    except ValueError:
        continue
    except KeyError:
        continue
total_invest.to_excel(os.getcwd() + "\투자지표데이터xls")
# financial_statements(code_data)
# financial_ratio(code_data)
# investment_indicators(code_data)
