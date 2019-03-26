import pandas as pd 

df = pd.read_excel('D:\Source\Python\pandas\Colling_Data_Excel.xlsx', sheet_name='Sheet1')

df['제  목'] = '해경 우리가 이겼다.'

print(df)
