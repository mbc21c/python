from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup
import datetime



def get_naver_news(query, s_date, e_date, s_from, e_to):
    url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=1&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
    #header 추가
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }
    req = uReq(url)

    return req

now = datetime.datetime.now()
nowDate = now.strftime('%Y-%m-%d')

yesterday = now - datetime.timedelta(days=1)
yesterdayDate = yesterday.strftime('%Y-%m-%d')

query = "해양경찰"   # url 인코딩 에러는 encoding parse.quote(query)
s_date = yesterdayDate
e_date = nowDate
s_from = s_date.replace("-","")
e_to = e_date.replace("-","")
page = 1

f = open("C:/aa/" + query + '_' + str(e_to) + '.txt', 'w', encoding='utf-8')

while page < 500:
    cont = get_naver_news(query, s_date, e_date, s_from, e_to)
    print(cont.read())
    soup = BeautifulSoup(cont, 'html.parser')
    print(soup)

    for urls in soup.select("._sp_each_url"):
        try :
            #print(urls["href"])
            if urls["href"].startswith("http://"):
                #print(urls["title"])
                #news_detail = get_news(urls["href"])
                    # pdate, pcompany, title, btext
                print("\n{}\n{}\n".format(urls["title"], urls["href"]))
                f.write("\n{}\n{}\n".format(urls["title"], urls["href"]))  # new style
        except Exception as e:
            print(e)
            continue
    page += 10


f.close()