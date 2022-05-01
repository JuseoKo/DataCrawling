from bs4 import BeautifulSoup
import requests
import re
import pandas as pd

file_path = './New/Data.csv'
frame = ''
data_count = 0
#최근 년도
days = 202205
#몇개월치 크롤링할지 정하기
month = 1
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

def urls(dayss):
    # 고정변수
    url_add = 'https://www.inews24.com'
    url_list = []
    url_day = []

    for k in range(0,month):
        #주소 결정변수 , range가 달력(월)수
        page = 1
        day = dayss[k]
        for j in range(0,70):
            #주소결정 range가 페이지수
            pages = page+j
            url = 'https://www.inews24.com/list/it?date='+str(day)+'&page='+str(pages)+''
            #파싱
            ress = requests.get(url)
            soup = BeautifulSoup(ress.content, 'html.parser')
            for i in range(0,30):
                #range가 주소 저장수
                try:
                    data = soup.select('body > main > article > ol > li:nth-child('+str(i+1)+') > div > a')[0].get('href')
                    url_list.append(url_add+data)
                    url_day.append(day)
                    print(f'저장년도 : {url_day[-1]}, 저장주소 : {url_list[-1]}')
                except IndexError:
                    break
    #중복제거
    url_list = set(url_list)
    url_list = list(url_list)
    inews(url_list, url_day)



#아이뉴스
def inews(url_list, url_day):
    for i in range(0,9999):
        try:
            #변수
            reur = requests.get(url_list[i])
            add_day = url_day[i]
            #파싱
            soup = BeautifulSoup(reur.content, 'html.parser')
            news_data = soup.select('#articleBody > p')
            data_def = re.sub('아이뉴스(.+?)기자','',str(news_data))
            data_def = preprocessing(data_def)
            print(f'Day : {add_day} 데이터 : {data_def}')
            save(data_def, add_day)
        except IndexError:
            break

#저장
def save(in_data, day):
    global data_count, frame
    #데이터 추가
    frame.loc[data_count, 'text'] = in_data
    #년도 추가
    frame.loc[data_count, 'day'] = str(day)
    frame.to_csv(file_path, encoding='utf-8-sig')
    data_count += 1

#데이터프레임(csv) 불러오기
def dataframe():
    global frame
    try:
        frame = pd.read_csv(file_path, index_col = 0)
    except:
        data = {
            'text' : [],
            'day' : []
        }
        frame = pd.DataFrame(data)
        frame.to_csv(file_path, encoding='utf-8-sig')
    return frame

def day():
    global days
    days_list = []
    for i in range(0,month):
        if days%100 == 1:
            days = days-89
        else:
            days = days-1
        days_list.append(days)
    return days_list
dataframe()
urls(day())
print(frame)
