import requests
import bs4
import pandas as pd

url = 'https://news.google.com/search?q=%ED%95%B4%EC%96%91%EA%B2%BD%EC%B0%B0%20when%3A1d&hl=ko&gl=KR&ceid=KR%3Ako'

resp = requests.get(url)
print(resp.text)
soup = bs4.BeautifulSoup(resp.text, 'html.parser')

print(soup)

items = soup.select('cwiz > div > div > div > div > main > c-wiz > div > div > div > article > h3')
print(items)
titles = []
links = []
for item in items:
    title = item.text
    link = item.get('href')
    titles.append(title)
    links.append(link)

data = {'title':titles, 'link':links}
df = pd.DataFrame(data, columns=['title', 'link'])
df.to_excel('./google_news_crolling.xlsx')