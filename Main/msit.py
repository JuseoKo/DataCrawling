import re
import time
from selenium import webdriver
import pandas as pd
from selenium.webdriver.common.by import By

#각종 변수선언
if True:
    #크롬드라이버 관련
    #크롬 경로
    options = webdriver.ChromeOptions()
    options.binary_location = "/Users/maria/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"
    #크롬 드라이버 경로
    chrome_driver_binary = "/Users/maria/Desktop/Code/capstone_3/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    #URL 과 RSS 데이터를 몇개 받아올지 갯수
    file_path = '../New/Gb.csv'
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
    data_def = re.sub('과학기술정보통신부','',str(data_def))
    data_def = re.sub('보 도 자 료','',str(data_def))
    data_def = re.sub('배포 일시','',str(data_def))
    data_def = re.sub('담당 부서','',str(data_def))
    data_def = re.sub('책임자','',str(data_def))
    data_def = re.sub('팀장','',str(data_def))
    data_def = re.sub('\((.+?)\)','',str(data_def))
    data_def = re.sub('담당자','',str(data_def))
    data_def = re.sub('사무관','',str(data_def))
    data_def = data_def.strip()
    return data_def
#년 계산
def year(day_data):
    year_data = re.sub('-(.+?)*', '', day_data)
    return year_data
#월계산
def month(day_data):
    month_data = re.search('-(.+?)-', day_data)
    month_data = month_data.group(1)
    return month_data
#저장
def save(in_data, year, month, add_line):
    global j, frame
    #데이터 추가
    frame.loc[add_line, 'text'] = in_data
    #년도 추가
    frame.loc[add_line, 'year'] = str(year)
    frame.loc[add_line, 'month'] = str(month)
#데이터프레임(csv) 불러오기
def dataframe():
    global frame
    try:
        frame = pd.read_csv(file_path, index_col = 0)
        frame = frame.astype({'year': 'str', 'month': 'str'})
    except:
        data = {
            'text' : [],
            'year' : [],
            'month' : []
        }
        frame = pd.DataFrame(data)
        frame.to_csv(file_path, encoding='utf-8-sig')
    return frame
def data():
    driver.switch_to.frame("iframe01")
    driver.switch_to.frame("innerWrap")
    data = driver.find_element(by=By.XPATH,value='//*[@id="content_body"]').text
    data = preprocessing(data)
    return data

def main():
    line = 0
    for j in range(1, 1169):
        url = 'https://www.msit.go.kr/bbs/list.do?sCode=user&mId=113&mPid=112&pageIndex='+str(j)+'&bbsSeqNo=94&nttSeqNo=&searchOpt=ALL&searchTxt='
        #중간저장
        if j%1000 == 0:
            frame.to_csv(file_path, encoding='utf-8-sig')
        for i in range(1, 11):
            try:
                driver.get(url)
                day = driver.find_element(by=By.XPATH, value='//*[@id="td_PSTG_BGNG_DT_'+str(i-1)+'"]').text
                driver.find_element(by=By.XPATH,value='//*[@id="result"]/div[2]/div['+str(i)+']/a').click()
                time.sleep(3.5)
                text_data = data()
                years = year(day)
                months = month(day)
                print(f'성공 : {driver.current_url}')
                line = line+1
                print(f'{years}년 {months}월 {line}번째 데이터 : {text_data}')
                save(text_data, years, months, line)
            except:
                print(f'실패 page : {j} 데이터 번호 : {i}')
                break
if __name__ == '__main__':
    dataframe()
    main()
    frame.to_csv(file_path, encoding='utf-8-sig')
    print(frame)