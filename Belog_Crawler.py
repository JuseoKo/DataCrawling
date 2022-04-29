from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
import feedparser
import pandas as pd
import datetime

#각종 변수선언
if True:
    #데이터 저장 관련
    frame = ''
    data_count = 0
        #날짜와 경로
    day = datetime.date.today()
    file_path = './Data/Belog/Belog '+str(day)+'.csv'

    #크롬드라이버 관련
    #크롬 경로
    options = webdriver.ChromeOptions()
    options.binary_location = "/Users/maria/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"
    #크롬 드라이버 경로
    chrome_driver_binary = "/Users/maria/Desktop/Code/capstone_3/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    #URL 과 RSS 데이터를 몇개 받아올지 갯수
    url = 'https://velog.io/recent'
    rss_url = 'https://v2.velog.io/rss/'
    rss_scroll_num = 1
    rss_list = []
# Rss주소 긁어오기
def Rss_search():
    global rss_list
    #Rss 데이터 수
    driver.implicitly_wait(10)
    for j in range(0, rss_scroll_num):
        driver.execute_script(f"window.scrollTo(0, 1000*{j})")
        time.sleep(2)

    #수프 이용을 위해 파싱
    htmls = driver.page_source
    soup = BeautifulSoup(htmls, 'html.parser')
    href = soup.prettify()
    href = re.findall('/@(.+?)/', href)
    #중복제거
    href = set(href)
    href = list(href)
    return href
#데이터 추출
def Data(Rss):
        for i in range(0, len(Rss)):
            Data_url = rss_url + Rss[i]
            print(Data_url)
            feed = feedparser.parse(Data_url)
            j = -1
            print(Rss)
            for k in feed['entries'] :
                j = j+1
                try:
                    data = feed['entries'][j]['summary']
                    data = preprocessing(data)
                    if data == '':
                        continue
                    print(data)
                    save(data)
                except KeyError:
                    continue
#전처리
def preprocessing(data):
    data_def = re.sub('<(.+?)>', '',str(data))
    data_def = re.sub('\r', '', str(data_def))
    data_def = re.sub('\t', '', str(data_def))
    data_def = re.sub('\n', '', str(data_def))
    data_def = re.sub('\f', '', str(data_def))
    data_def = re.sub('\v', '', str(data_def))
    data_def = re.sub('\[', '', str(data_def))
    data_def = re.sub('\]', '', str(data_def))
    data_def = data_def.strip()
    return data_def
#저장
def save(data):
    global data_count, frame
    #데이터 추가
    frame.loc[data_count] = data
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

if __name__ == '__main__' :
    #실행
    driver.get(url)
    frames = dataframe()
    #데이터 가져오기
    Data(Rss_search())


# htmls = driver.page_source
# soup = BeautifulSoup(htmls, 'html.parser')
# data = soup.prettify()
# print(data)
# last_data = re.findall('/@(.+?)/', data)
# print(last_data)