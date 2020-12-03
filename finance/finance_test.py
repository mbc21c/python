import requests
from bs4 import BeautifulSoup
import pandas as pd

stock_dict={}
url = "https://www.sedaily.com/Stock/Quote?type=1"

try:
    html = requests.get(url)
except requests.exceptions.RequestException as e:
    print(e)
else:
    soup = BeautifulSoup(html.text, "lxml")

all_table=soup.find_all('div',{'class':'table'})

for thead in all_table:
    dl=thead.find('dl', {'class':'thead'})
    dt=dl.find('dt')
    fieldName=dt.text

    tbody=thead.find_all('dl',{'class':'tbody'})

    for dl in tbody:

        name = dl.find('dt').get_text()
        dd = dl.find('dd')
        code = dd.get('id').replace('dd_Item_','')
        price = dd.find('span').get_text().replace(',','')
        stock_dict[code] = [name, fieldName, price]

print(stock_dict)