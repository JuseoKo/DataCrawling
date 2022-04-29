import requests
from bs4 import BeautifulSoup
import re
import time
import keyboard

#변수선언
if True:
    # 반복횟수 카운트 변수
    count = 0
    #반복을 위한 변수
    crawler_start = False
    # 주소값 변수
    week_url = 'https://velog.io'
    new_url = 'https://velog.io/recent'
    #txt파일 경로
    new_file_path = "Data/실시간.txt"
    week_file_path = "Data/주간랭킹.txt"
    new_list = []
    week_list = []

#실시간, 주간랭킹 파일 오픈하고 리스트에 저장
def address_flie_open():
    global new_list, week_list, new_file_path, week_file_path
    #새로운글 저장을 위한 배열(이전 저장파일 로드)
    with open(new_file_path) as new_load:
        new_list = new_load.read().splitlines()

    #주간글 저장을 위한 배열(이전 저장파일 로드)
    with open(week_file_path) as new_load:
         week_list = new_load.read().splitlines()

#주간랭킹글 긁어오기
def week_address():
    global week_url, week_list, new_file_path
    #객체준비와 한글깨짐을 방지하기 위해 인코딩
    week_response = requests.get(week_url)
    week_soup = BeautifulSoup(week_response.content, 'html.parser', from_encoding='cp949')
    try:
        # 주간 인기글 25개 긁어오기
        for i in range(0, 20) :
            #  선택 경로안에 있는 href 테그만 25개를 불러옴
            week_href = week_soup.select('#root > div.sc-dPiLbb > div.sc-bqiRlB.eeKvZX > div.sc-bBHHxi.iFCgdF > main.sc-cNKqjZ.frPFLP > div.sc-eJwWfJ.hPOjoM > div.sc-jgrJph.fubVJV > a.sc-hUpaCq.keJMFL')[i].get("href")
            # rss활용을 위해 아이디만 뽑아내는 정규식(주간)
            week_add = re.search('/@(.+?)/', week_href)
            week_data = week_add.group(1)
            week_result = 'https://v2.velog.io/rss/' + week_data
            #위에 만들어둔 배열에 저장
            week_list.append(week_result)
    except:
        print('주간 인기글을 불러오지 못했습니다.')
    #중복제거
    x = set(week_list)
    week_list = list(x)

#최신글 긁어오기
def new_address():
    global new_list, new_url, count, Crawler_start
    while not crawler_start:
        #프로그램 중지
        keyboard.add_hotkey('space', lambda: Crawler_end())

        #새로고침
        new_response = requests.get(new_url)
        new_soup = BeautifulSoup(new_response.content, 'html.parser', from_encoding='cp949')

        #카운트+데이터 가져오기
        count = count+1
        try:
            for i in range(0,5) :
                new_href = new_soup.select('#root > div.sc-dPiLbb > div.sc-bqiRlB.eeKvZX > div.sc-bBHHxi.iFCgdF > main.sc-cNKqjZ.frPFLP > div.sc-eJwWfJ.hPOjoM > div.sc-jgrJph.fubVJV > a.sc-hUpaCq.keJMFL')[i].get("href")
                new_add = re.search('/@(.+?)/', new_href)
                new_data = new_add.group(1)
                new_result = 'https://v2.velog.io/rss/' + new_data
                new_list.append(new_result)
                continue
        except:
            print("데이터 수 초과")
        #중복제거
        x = set(new_list)
        new_list = list(x)
        print(f"\n중지하려면 스페이스바를 누르세요(누른 이후 2분뒤 종료됩니다) \n반복횟수 : {count} \n실시간 데이터 수 : {len(new_list)}")
        #대기시간
        time.sleep(2)

#프로그램 종료
def Crawler_end():
    global crawler_start
    crawler_start = True

#주소저장
def address_save():
    global new_list, week_list
    #실시간 주소 저장
    with open(new_file_path,'w',encoding='UTF-8') as new:
        for new_name in new_list:
            new.write(new_name+'\n')
    #주간랭킹 주소 저장
    with open(week_file_path,'w',encoding='UTF-8') as week:
        for week_name in week_list:
            week.write(week_name+'\n')

#실행
if __name__ == '__main__':
    address_flie_open()

    print(f'실시간 데이터 : {new_list} \n데이터 수 : {len(new_list)}')
    print(f'주간랭킹 데이터 : {week_list} \n데이터 수 : {len(week_list)}')

    week_address()
    new_address()
    address_save()
    #결과출력
    print(f'\n__결과__\n실시간 데이터 수 : {len(new_list)}')
    print(f'주간랭킹 데이터 수 :{len(week_list)}')
