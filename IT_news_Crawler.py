import requests
from bs4 import BeautifulSoup
import re
import feedparser

#변수
file_path = './Data/News.txt'
# 경향일보, 아이뉴스, 한경닷컴, it동아, it비즈,파이낸셜,디데일리
#중앙일보는 주소가 존재하지 않음
rss = ['http://www.khan.co.kr/rss/rssdata/it_news.xml',
       'http://www.inews24.com/rss/news_it.xml',
       'https://rss.hankyung.com/feed/it.xml',
       'https://it.donga.com/feeds/rss/news/',
       'https://www.itbiznews.com/rss/S1N3.xml',
       'http://www.fnnews.com/rss/new/fn_realnews_it.xml',
       'http://www.ddaily.co.kr/DATA/rss/ddaily_rss_itpolicy.xml',
       'https://rss.hankooki.com/daily/dh_it_tech.xml'
       ]

#텍스트 추출구조
#경향
def khan():
       news_data = soup.select('#articleBody > p.content_text')
       data_def = re.sub('<(.+?)>', '',str(news_data))
       return data_def
#아이뉴스
def inews():
       news_data = soup.select('#articleBody > p')
       data_def = re.sub('<(.+?)>', '',str(news_data))
       return data_def
#한경
def hankyung():
       news_data = soup.select('#articletxt')
       data_def = re.sub('<(.+?)>', '',str(news_data))
       return data_def
#동아일보
def donga():
       news_data = soup.select('body > main > div > div.main-content.col-lg-8 > div.article > article > p')
       data_def = re.sub('<(.+?)>', '',str(news_data))
       return data_def
#it비즈
def itbiz():
       news_data = soup.select('#article-view-content-div > p')
       data_def = re.sub('<(.+?)>', '',str(news_data))
       return data_def
#파이낸셜
def fnnews():
       news_data = soup.select('#article_content')[0].get_text()
       data_def = re.sub('\[(.+?)\]', '',str(news_data))
       data_def = re.sub('※(.+?)지', '',str(data_def))
       data_def = re.sub('/(.+?)뉴스1', '',str(data_def))
       return data_def
#디지털데일리
def ddaily():
       data_def = soup.select('#news_body_area')[0].get_text()
       return data_def
#한국 수정해야됨
def hankooki():
       global soup
       url_plu = soup
       url_plu = re.search('/(.+?)"', str(url_plu))
       url_plu = url_plu.group()
       url_plu = re.sub('"','',url_plu)
       main_url = 'http://daily.hankooki.com' + url_plu
       print(main_url)

       response = requests.get(main_url, headers={"User-Agent": "Mozilla/5.0"})
       soup = BeautifulSoup(response.content, 'html.parser')
       data = soup.select('#article-view-content-div > p')
       data = re.sub('<(.+?)>','', str(data))
       return data
#뉴스 종류별 회전
def ring():
       #0 = 경한, 1 = 중앙,
       if a == 0 :
              data = khan()
       elif a == 1 :
              data = inews()
       elif a == 2 :
              data = hankyung()
       elif a == 3 :
              data = donga()
       elif a == 4:
              data = itbiz()
       elif a == 5:
              data = fnnews()
       elif a == 6:
              data = ddaily()
       elif a == 7:
              data = hankooki()
       return data

#저장
def save(data):
       for k in range(0, len(url_list)):
              f = open(file_path,'a')
              f.write(data)

#rss주소를 돌아가면서 세팅하기, url_list 초기화
if __name__ == '__main__':
       for a in range(0, len(rss)) :
              url = feedparser.parse(rss[a])
              url_list = []
              #뉴스 url 불러오기
              for i in url.entries :
                     url_list.append(i.link)

              #수프 재세팅
              for j in range(0, len(url_list)) :
                     response = requests.get(url_list[j], headers={"User-Agent": "Mozilla/5.0"})
                     soup = BeautifulSoup(response.content, 'html.parser')
                     data = ring()
                     print(data)
                     save(data)
