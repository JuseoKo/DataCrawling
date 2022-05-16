from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import pandas as pd
import re
import datetime

#각종 변수선언
if True:
    #크롬드라이버 관련
    #크롬 경로
    options = webdriver.ChromeOptions()
    options.binary_location = "/Users/maria/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"
    #크롬 드라이버 경로
    chrome_driver_binary = "/Users/maria/Desktop/Code/capstone_3/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    #공통변수
    #날짜와 경로
    day = datetime.date.today()
    file_path = './Data/Work/Work '+str(day)+'.csv'
    #주소를 담아둘 배열
    url_list = []
    #저장과 불러오기 관련 변수
    data_count = 0
    frame = ''

    #원티드 변수 선언
    #스크롤 횟수
    wanted_scroll_num = 10
    #url
    wanted_url = 'https://www.wanted.co.kr/wdlist?country=kr&job_sort=job.latest_order&years=-1&locations=all'
    #페이지의 구조
    wanted_text_value = ['//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[2]',
                         '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[3]',
                         '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[4]']

    # 프로그래머스 변수 선언
    #페이지 수
    programers_page_num = 10
    #url
    programers_url = 'https://programmers.co.kr/job?page='
    # 페이지 구조
    programers_text_value = ['/html/body/div[3]/div/div[1]/div/div[1]/section[2]',
                             '/html/body/div[3]/div/div[1]/div/div[1]/section[3]',
                             '/html/body/div[3]/div/div[1]/div/div[1]/section[4]',
                             '/html/body/div[3]/div/div[1]/div/div[1]/section[5]',]
#원티드
def wanted() :
    #url로드기능
    driver.get(wanted_url)
    time.sleep(3)
    #추출할 웹사이트 갯수를 range로 표현함 , url 로드기능
    for i in range(0, 10000) :
        #스크롤 내림
        if i == 0 :
            for j in range(0 ,wanted_scroll_num):
                driver.execute_script(f"window.scrollTo(0, 1000*{j})")
                time.sleep(1.5)
        try:
            #path 경로설정
            count = str(1+i)
            path = '//*[@id="__next"]/div[3]/div/div/div[3]/ul/li['+count+']/div/a'
            #path 경로에 있는 href태그만 가져오기
            url_data = driver.find_element(by=By.XPATH, value=path).get_attribute('href')
            #태그 리스트로 저장
            url_list.append(url_data)
            #더이상 url 데이터가 없으면 루프문 탈출
        except:
            break
    #데이터 로드기능
    load(wanted_text_value)
    #리스트 초기화
    url_list.clear()

#프로그래머스
def programers():
    #url로드기능
    #페이지 설정
    count_page = 0
    for j in range(0, programers_page_num) :
        #url설정 , 접속
        count_page = count_page + 1
        programers_url_set = programers_url + str(count_page)
        driver.get(programers_url_set)
        time.sleep(5)

        for i in range(0, programers_page_num*20):
            try:
                count = str(1+i)
                path = '//*[@id="list-positions-wrapper"]/ul/li['+count+']/div[2]/h5/a'
                url_data = driver.find_element(by=By.XPATH,value=path).get_attribute('href')
                url_list.append(url_data)
            except:
                break

    #데이터 로드
    load(programers_text_value)
    #리스트 초기화
    url_list.clear()

#데이터 로드기능
def load(value):
    # 데이터 로드기능
    for k in range(0, len(url_list)) :
        #찾은 주소로 들어가기(로딩대기)
        driver.get(url_list[k])
        driver.implicitly_wait(10)
        driver.execute_script(f"window.scrollTo(0, 500)")
        time.sleep(0.5)
        in_data = ''
        try:
            #해당 경로에 있는 텍스트 긁어오기
            for i in range(0, 3):
                try:
                    data_add = driver.find_element(by=By.XPATH, value=value[i]).text
                except:
                    continue
                in_data = in_data + data_add
        except:
            #로딩이 제대로 안된채로 긁어오면 에러발생 (재로딩)
            driver.get(url_list[k])
            time.sleep(3)
            for i in range(0, 3):
                data_add = driver.find_element(by=By.XPATH, value=value[i]).text
                in_data = in_data + data_add
                #줄바꿈 제
        #in_data 변수에 글자(str)이 들어있으니 원하는 저장포맷으로 저장하기
        save(in_data)
    #리스트 초기화
    url_list.clear()

#저장
def save(in_data):
        global data_count, frame
        #줄바꿈 제거
        in_data = re.sub('\n','',str(in_data))
        #데이터 추가
        frame.loc[data_count] = in_data
        frame.to_csv(file_path, encoding='utf-8-sig')
        data_count += 1

#데이터프레임(csv) 불러오기
def dataframe():
    global frame
    try:
        frame = pd.read_csv(file_path, index_col = 0)
    except:
        data = {
            'text' : []
        }
        frame = pd.DataFrame(data)
        frame.to_csv(file_path, encoding='utf-8-sig')
    return frame


#메인
if __name__ == '__main__' :
    # 데이터 프레임 불러오기
    frames = dataframe()

    # 원티드 채용 사이트
    wanted()

    # #프로그래머스 채용 사이트
    programers()
    print(frames)

#로딩속도때문에 데이터가 안뜨는거임 즉 로딩이 시작되기 전엔 데이터가 존재하지 않음
#최종 데이터는 in_data 함수에 존재함
#scroll_num 변수의 숫자를 바꾸면서 추가 데이터 로딩횟수 조절가능
