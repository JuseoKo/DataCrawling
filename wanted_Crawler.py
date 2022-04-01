from selenium import webdriver
from selenium.webdriver.common.by import By
import time

#각종 변수선언
if True:
    #크롬 경로
    options = webdriver.ChromeOptions()
    options.binary_location = "/Users/maria/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"

    #크롬 드라이버 경로
    chrome_driver_binary = "/Users/maria/Desktop/Code/capstone_3/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    #변수선언
    #주소를 담아둘 배열
    url_list = []
    #데이터 페이지의 구조
    text_value = '//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section'
    #스크롤 횟수
    scroll_num = 10

    #url
    url = 'https://www.wanted.co.kr/wdlist?country=kr&job_sort=job.latest_order&years=-1&locations=all'

#url불러오기
def url_road() :
    #추출할 웹사이트 갯수를 range로 표현함
    for i in range(0, 10000) :
        #스크롤 내림
        if i == 0 :
            for j in range(0 ,scroll_num):
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
    print(url_list)
#데이터 불러오기
def data_road() :
    for i in range(0, len(url_list)) :
        # #찾은 주소로 들어가기(로딩대기)
        driver.get(url_list[i])
        try:
            #해당 경로에 있는 텍스트 긁어오기
            in_data = driver.find_element(by=By.XPATH, value=text_value).text
        except:
            #로딩이 제대로 안된채로 긁어오면 에러발생 (재로딩)
            print('재로딩')
            driver.get(url_list[i])
            time.sleep(2)
            in_data = driver.find_element(by=By.XPATH, value=text_value).text
        #in_data 변수에 글자가 들어있으니 원하는 저장포맷으로 저장하기
        print(f'결과 \n{in_data} \n{i}\n')
#메인
if __name__ == '__main__' :
    #원티드 채용 사이트 열고 로딩대기
    driver.get(url)
    time.sleep(5)
    url_road()
    data_road()

#로딩속도때문에 데이터가 안뜨는거임 즉 로딩이 시작되기 전엔 데이터가 존재하지 않음
#최종 데이터는 in_data 함수에 존재함
#scroll_num 변수의 숫자를 바꾸면서 추가 데이터 로딩횟수 조절가능