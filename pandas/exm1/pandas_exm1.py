import pandas as pd 

df = pd.read_excel('mandoo.xlsx')



def double_num(num):
    return num * 2

df['doubled'] = df['만두생산'].apply(double_num)

wr = pd.ExcelWriter('new_book.xlsx')
df.to_excel(wr, 'new_sheet')
wr.save()

print(df.head())
