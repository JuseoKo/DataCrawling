from bs4 import BeautifulSoup
import requests
import re
import pandas as pd
#변수선언
if True:
    #okky 의 페이지 수
    page = 6073
    file_path = '../New/okky_Data.csv'
    frame = ''
    #마지막 데이터 줄 + 1
    # line = 5070
    line = 120126
def main(url_list):
    for i in range(line, 999999):
        try:
            #변수
            red = requests.get(url_list[i])
            soup = BeautifulSoup(red.content, 'html.parser')

            #월, 년 변수
            day_data = soup.select('#article > div.panel.panel-default.clearfix.fa- > div.panel-heading.clearfix > div.avatar.clearfix.avatar-medium.pull-left > div > div.date-created > span')
            day_data = re.search('title="(.+?)T',str(day_data))
            day_data = day_data.group(1)
            add_year = year(day_data)
            add_month = month(day_data)
            #메인 데이터
            main_data = soup.select('#content-body > article')
            main_data = preprocessing(main_data)
            print(f'데이터 번호 : {i}')
            save(main_data, add_year, add_month, i)
            if i%3000 == 0:
                frame.to_csv(file_path, encoding='utf-8-sig')
                print('저장')
        except AttributeError:
            continue
        except :
            frame.to_csv(file_path, encoding='utf-8-sig')
            print('에러')
            break

#url 불러와서 텍스트로 저장
def url_add():
    global page
    link_num = 24
    url_list = []
    for j in range(0,page):
        url_add = 'https://okky.kr/article/'
        num = j*link_num
        url = 'https://okky.kr/articles/community?offset='+str(num)+'&max=24'
        print(url)
        ress = requests.get(url)
        soup = BeautifulSoup(ress.content, 'html.parser')
        print(f'남은 작업 : {j+1}/{page}')
        for i in range(1, 25):
            data = soup.select('#list-article > div.panel.panel-default.community-panel > ul > li:nth-child('+str(i)+') > div.list-title-wrapper.clearfix > div > span')
            data = re.search('#(.+?)<', str(data))
            data = data.group(1)
            url_list.append(url_add+data)

    url_list = set(url_list)
    url_list = list(url_list)
    for i in range(0, len(url_list)):
        f = open('../Okky_Link.txt', 'a')
        f.write(f'{url_list[i]}\n')
    f.close()
#텍스트 파일로 저장된 url 불러오기
def url_load():
    f = open('../Okky_Link.txt', 'r')
    data = f.readlines()
    #\n제거
    data = [i.strip() for i in data]
    print(len(data))
    return data
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
    global data_count, frame
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
    # url_add()
    dataframe()
    data = url_load()
    main(data)
    print(frame)
    frame.to_csv(file_path, encoding='utf-8-sig')