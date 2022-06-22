from selenium import webdriver
from selenium.webdriver.common.by import By
import pandas as pd
import re

if True:
    #크롬드라이버 관련
    #크롬 경로
    options = webdriver.ChromeOptions()
    options.binary_location = "/Users/maria/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"
    #크롬 드라이버 경로
    chrome_driver_binary = "/Users/maria/Desktop/Code/capstone_3/chromedriver"
    driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)

    #url 번호카운트 , 데이터 xpath,날짜 데이터 xpath, 데이터 프레임 생성, 데이터 저장경로,
    line = 25000
    value = '/html/body/div/div[2]/div[5]/div/table[5]/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td'
    value_2 = '/html/body/div/div[2]/div[5]/div/table[2]/tbody/tr[3]/td/table/tbody/tr/td[5]/div/div[1]'
    frame : ''
    file_path = '../New/ppomppu.csv'
    #데이터 저장 포맷 설정


#메인
def main():
    for i in range(line, 25100):
        try:
            url = 'https://www.ppomppu.co.kr/zboard/view.php?id=developer&page=1&divpage=5&no='+str(i)+''
            driver.get(url)
            data = driver.find_element(by=By.XPATH, value=value).text
            data = preprocessing(data)
            day = driver.find_element(by=By.XPATH, value=value_2).text
            day = re.search('등록일: (.+?) ', day)
            day = day.group(1)
            years = year(day)
            months = month(day)
            if data == '':
                print(f'{i}번째 데이터 없음')
                continue
            else:
                print(f'{i}번째 성공')
                print(f'데이터 번호 : {i}, 내용 : {data}')
                save(data, years, months, i)
                frame.to_csv(file_path, encoding='utf-8-sig')
            if i%3000 == 0:
                frame.to_csv(file_path, encoding='utf-8-sig')
                print('저장')
        except :
            continue


#년 계산
def year(day_data):
    year_data = re.sub('-(.+?)*', '', day_data)
    return year_data
#월계산
def month(day_data):
    month_data = re.search('-(.+?)-', day_data)
    month_data = month_data.group(1)
    return month_data
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
if __name__ == '__main__':
    dataframe()
    main()
    frame.to_csv(file_path, encoding='utf-8-sig')
    print(frame)

