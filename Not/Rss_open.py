from Not import Belog_Crawler
import re
import requests
from bs4 import BeautifulSoup

#파일 오픈해서 리스트 받아오기
Belog_Crawler.address_flie_open()
urllist_week = Belog_Crawler.week_list
urllist_day = Belog_Crawler.new_list

# #변수생성
file_path_week = 'Data/주간데이터.txt'
file_path_day = 'Data/일간데이터.txt'


#객체생성 + 반복문
for i in range(0, len(urllist_week)):
    link_list = urllist_week[i]
    url = link_list
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding='cp949').text

    #> < 사이에 있는 모든태그 제거후 리스트로 만들기
    add = re.findall('>(.+?)<', soup)
    #리스트를 텍스트로 변환
    list_Change = ''
    for i in add:
        list_Change += i + " "
    #남은 태그 제거
    result = re.sub('<(.+?)>', ' ', list_Change)



    #남은 태그 제거
    result = re.sub('<(.+?)>', ' ', list_Change)
    print(result)
    #파일저장
    f = open(file_path_week,'a')
    for k in range(0, len(urllist_week)):
        data = result
    f.write(data)


for i in range(0, len(urllist_day)):
    link_list = urllist_day[i]
    url = link_list
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser', from_encoding='cp949').text

    #> < 사이에 있는 모든태그 제거후 리스트로 만들기
    add = re.findall('>(.+?)<', soup)
    #리스트를 텍스트로 변환
    list_Change = ''
    for i in add:
        list_Change += i + " "
    #남은 태그 제거
    result = re.sub('<(.+?)>', ' ', list_Change)



    #남은 태그 제거
    result = re.sub('<(.+?)>', ' ', list_Change)
    print(result)
    f = open(file_path_day,'a')
    for k in range(0, len(urllist_day)):
        data = result
    f.write(data)