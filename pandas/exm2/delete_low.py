import pandas as pd 
df = pd.read_excel('data.xlsx')
df[::2].to_excel('even.xlsx')

