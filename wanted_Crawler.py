from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import requests
from bs4 import BeautifulSoup

#각종 변수선언
if True:
    #크롬 경로
    options = webdriver.ChromeOptions()
    options.binary_location = "/Users/maria/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"

    #크롬 드라이버 경로
    chrome_driver_binary = "/Users/maria/Desktop/Code/capstone_3/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    #공통변수선언
    file_path = './Data/Work.txt'
    #주소를 담아둘 배열
    url_list = []

    #원티드 변수 선언
    #페이지의 구조
    wanted_text_value = '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section'
    #스크롤 횟수
    wanted_scroll_num = 1
    #url
    wanted_url = 'https://www.wanted.co.kr/wdlist?country=kr&job_sort=job.latest_order&years=-1&locations=all'

    # 프로그래머스 변수 선언 페이지의 구조
    #번호 갯수
    programers_page_num = 2
    # 프로그래머스 주소
    programers_url = 'https://programmers.co.kr/job'

#원티드
#url불러오기
def wanted() :
    driver.get(wanted_url)
    time.sleep(3)
    #추출할 웹사이트 갯수를 range로 표현함 , url 로드기능
    for i in range(0, 10000) :
        #스크롤 내림
        if i == 0 :
            for j in range(0 ,wanted_scroll_num):
                driver.execute_script(f"window.scrollTo(0, 1000*{j})")
                time.sleep(1)
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
    # 데이터 로드기능
    for j in range(0, len(url_list)) :
        #찾은 주소로 들어가기(로딩대기)
        driver.get(url_list[j])
        try:
            #해당 경로에 있는 텍스트 긁어오기
            in_data = driver.find_element(by=By.XPATH, value=wanted_text_value).text
        except:
            #로딩이 제대로 안된채로 긁어오면 에러발생 (재로딩)
            print('재로딩')
            driver.get(url_list[j])
            time.sleep(2)
            in_data = driver.find_element(by=By.XPATH, value=wanted_text_value).text
        #in_data 변수에 글자가 들어있으니 원하는 저장포맷으로 저장하기
        save(in_data, url_list)
    #리스트 초기화
    url_list.clear()

#프로그래머스
#url불러오기
def programers():
    # programers_page = ''
    driver.get(programers_url+programers_page)
    time.sleep(5)
    for i in range(0, programers_page_num*20):
        try:
            count = str(1+i)
            path = '//*[@id="list-positions-wrapper"]/ul/li['+count+']/div[2]/h5/a'
            url_data = driver.find_element(by=By.XPATH,value=path).get_attribute('href')
            url_list.append(url_data)
        except:
            for j in range(0, programers_page_num):
                programers_page = '/job?page='+j
            # break
    print(url_list)

#저장
def save(data, url_len):
    for k in range(0, len(url_len)):
        f = open(file_path,'a')
        f.write(data)
#메인
if __name__ == '__main__' :
    # 원티드 채용 사이트
    # wanted()
    # #프로그래머스 채용 사이트
    programers()


#로딩속도때문에 데이터가 안뜨는거임 즉 로딩이 시작되기 전엔 데이터가 존재하지 않음
#최종 데이터는 in_data 함수에 존재함
#scroll_num 변수의 숫자를 바꾸면서 추가 데이터 로딩횟수 조절가능