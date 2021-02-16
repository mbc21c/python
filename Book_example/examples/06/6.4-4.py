﻿from openpyxl import load_workbook

# result.xlsx를 읽은 후 기본 시트를 선택
xlsx = load_workbook('result.xlsx', read_only=True)
sheet = xlsx.active

# 1~2 행을 가져옴
rows = sheet['1:2']
# 각 행을 가져오기 위한 반복문
for row in rows:
    # 각 행의 셀을 가져오기 위한 반복문
    for cell in row:
        print(cell.value)

