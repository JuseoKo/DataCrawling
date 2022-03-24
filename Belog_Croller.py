import requests
from bs4 import BeautifulSoup
import re
import time
import keyboard

#프로그램 정지를 위한 함수
def new_end():
    global new_start
    new_start = True
    return


# 반복횟수 카운트 변수
count = 0
#반복을 위한 변수
new_start = False
# 주소값 변수
week_url = 'https://velog.io'
new_url = 'https://velog.io/recent'


#객체준비와 한글깨짐을 방지하기 위해 인코딩
week_response = requests.get(week_url)
week_soup = BeautifulSoup(week_response.content, 'html.parser', from_encoding='cp949')
week_list = [] # 한주의 인기글 저장을 위한 배열
new_list = [] #새로운글 저장을 위한 배열


# 주간 인기글 25개 긁어오기
for i in range(0, 24) :
    #  선택 경로안에 있는 href 테그만 25개를 불러옴
    week_href = week_soup.select('#root > div.sc-dPiLbb > div.sc-bqiRlB.eeKvZX > div.sc-bBHHxi.iFCgdF > main.sc-cNKqjZ.frPFLP > div.sc-eJwWfJ.hPOjoM > div.sc-jgrJph.fubVJV > a.sc-hUpaCq.keJMFL')[i].get("href")
    # rss활용을 위해 아이디만 뽑아내는 정규식(주간)
    week_add = re.search('/@(.+?)/', week_href)
    week_data = week_add.group(1)
    week_result = 'https://v2.velog.io/rss/' + week_data
    #위에 만들어둔 배열에 저장
    week_list.append(week_result)


#최신글
while not new_start:
    #프로그램 중지
    keyboard.add_hotkey('space', lambda: new_end())

    #새로고침
    new_response = requests.get(new_url)
    new_soup = BeautifulSoup(new_response.content, 'html.parser', from_encoding='cp949')

    #카운트+데이터 가져오기
    count = count+1
    print(f"중지하려면 스페이스바를 누르세요 \n반복횟수 : {count}")
    for i in range(0,5) :
        new_href = new_soup.select('#root > div.sc-dPiLbb > div.sc-bqiRlB.eeKvZX > div.sc-bBHHxi.iFCgdF > main.sc-cNKqjZ.frPFLP > div.sc-eJwWfJ.hPOjoM > div.sc-jgrJph.fubVJV > a.sc-hUpaCq.keJMFL')[i].get("href")
        new_add = re.search('/@(.+?)/', new_href)
        new_data = new_add.group(1)
        new_result = 'https://v2.velog.io/rss/' + new_data
        new_list.append(new_result)
        continue
    #대기시간
    time.sleep(300)

#중복제거
x = set(week_list)
week_list = list(x)
x = set(new_list)
new_list = list(x)


#결과출력
print(f'실시간 : {new_list}')
print(f'갯수 : {len(new_list)}')
print(f'주간인기 : {week_list}')
print(f'갯수 :{len(week_list)}')


#실시간 주소 저장
with open('실시간.txt','w',encoding='UTF-8') as new:
    for new_name in new_list:
        new.write(new_name+'\n')
#주간랭킹 주소 저장
with open('주간랭킹.txt','w',encoding='UTF-8') as week:
    for week_name in week_list:
        week.write(week_name+'\n')