import requests
from bs4 import BeautifulSoup
import datetime
import os


def get_naver_news(query, s_date, e_date, s_from, e_to):
    url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=1&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
    #header 추가
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }
    req = requests.get(url,headers=header)

    return req.content

def get_detail_news(urls):
    #header 추가
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }
    req_detail = requests.get(urls)
    #print(req_detail.content)
    return req_detail.content

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
filepath = "c:/aa/" + str(e_to)

if not(os.path.isdir(filepath)):
    os.makedirs(os.path.join(filepath))

#f = open(filepath + "/"+ query + '_' + str(e_to) + '.txt', 'w', encoding='utf-8')

while page < 500:
    cont = get_naver_news(query, s_date, e_date, s_from, e_to)
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
                cont_detail = get_detail_news(urls["href"])
                soup_detail = BeautifulSoup(cont_detail, 'html.parser')
                #print("soup_detail" + str(soup_detail))


                for tag in soup_detail.find_all("meta"):
                    if tag.get("property", None) == "og:title":
                        title = tag.get("content", None)
                    elif tag.get("property", None) == "og:description":
                        description = tag.get("content", None)

                print("\n{}\n{}\n".format(title, description))
                f = open(filepath + "/" + title + '.txt', 'w', encoding='utf-8')
                f.write("\n{}\n\n{}\n\n{}\n".format(title, urls["href"], description))
                f.close()
        except Exception as e:
            print(e)
        continue
    page += 10


