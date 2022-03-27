import Belog_Crawler
import re
import requests
from bs4 import BeautifulSoup

#rss 주소 객체 소환
Belog_Crawler.address_flie_open()
url_set = Belog_Crawler.week_list

#주소
url = 'https://v2.velog.io/rss/youn1201'
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='cp949').text

#> < 사이에 있는 모든태그 제거후 리스트로 만들기
add = re.findall('>(.+?)<', soup)
#리스트를 텍스트로 변환
list_Change = ''
for i in add:
    list_Change += i + " "
#남은 태그(url) 제거
result = re.sub('<img(.+?)alt="">', ' ', list_Change)
result = re.sub('<a(.+?)">', ' ', result)

#결과 출력
print(result)