import requests
from bs4 import BeautifulSoup
import datetime
import os

def get_naver_news(query, s_date, e_date, s_from, e_to, page):
    url = "https://search.naver.com/search.naver?where=news&query=" + query + "&sort=1&ds=" + s_date + "&de=" + e_date + "&nso=so%3Ar%2Cp%3Afrom" + s_from + "to" + e_to + "%2Ca%3A&start=" + str(page)
    #header 추가
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }
    req = requests.get(url)

    return req.content

def get_detail_news(urls):
    #header 추가
    header = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36',
    }
    req_detail = requests.get(urls)
    #print(req_detail.content)
    return req_detail.content

def croling_naver(str_keyword):
    now = datetime.datetime.now()
    nowdate = now.strftime('%y-%m-%d')

    yesterday = now - datetime.timedelta(days=2)
    yesterdaydate = yesterday.strftime('%y-%m-%d')

    page = 1
    query = str_keyword   # url 인코딩 에러는 encoding parse.quote(query)
    s_date = yesterdaydate
    e_date = nowdate
    s_from = s_date.replace("-","")
    e_to = e_date.replace("-","")
    filepath = "c:/aa/" + str(e_to)

    if not(os.path.isdir(filepath)):
        os.makedirs(os.path.join(filepath))

    f = open(filepath + '/' + query + '_' + str(e_to) + '.txt', 'w', encoding='utf-8')

    while page < 500:
        cont = get_naver_news(query, s_date, e_date, s_from, e_to, page)
        soup = BeautifulSoup(cont, 'html.parser')
        print(soup)
        cnt = 0

        for urls in soup.select("._sp_each_url"):
            try:
                if urls["href"].startswith("http://"):
                    print("\n{}\n".format(urls["href"]))
                    #print("\n{}\n{}\n".format(urls["title"], urls["href"]))
                    cont_detail = get_detail_news(urls["href"])
                    soup_detail = BeautifulSoup(cont_detail, 'html.parser')
                    for tag in soup_detail.find_all("meta"):
                        try:
                            if tag.get("property") == "og:title":
                                title = tag.get("content")
                            elif tag.get("property") == "og:description":
                                description = tag.get("content")
                            else:
                                title = str(cnt) + "." + urls["title"]
                                description = ''

                            cnt = cnt + 1 
                        except exception as e:
                            print(e)
                        continue


#                    print("\n{}\n{}\n".format(title, description))
                    print(title)
                    title = title.replace('"', '').replace('?', '').replace('\r', '').replace('\n', '').replace('<', '').replace('>', '').replace('/', '').replace('|', '').replace('·', '').replace('[', '').replace(']', '')
                    print(title)
                   # title = title.replace('/\r\n|\r|\n/', '')
                    f = open(filepath + "/" + title + '.txt', 'w', encoding='utf-8')
                    f.write("\n{}\n\n{}\n\n{}\n".format(title, urls["href"], description))
                    f.close()
            except exception as e:
                print(e)
            continue
        page += 10

croling_naver('해양경찰')