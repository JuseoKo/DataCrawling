import bs4
import requests
from bs4 import BeautifulSoup
import re
import feedparser
import pandas as pd
def preprocessing(data):
    data_def = re.sub('\r', '', str(data))
    data_def = re.sub('\t', '', str(data_def))
    data_def = re.sub('\n', '', str(data_def))
    return data_def

url = 'http://www.ddaily.co.kr/news/news_view.php?uid=110361'
#url 세팅
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
data_def = soup.select('#news_body_area')[0].get_text()
data_def = preprocessing(data_def)
#판다스
data = {
    'text' : []
}
frame = pd.DataFrame(data)
frame.loc[0] = data_def
frame.to_csv('./Data/test.csv', encoding='utf-8-sig')
print(frame)

# #판다스
# import pandas as pd
# import datetime
#
# day = datetime.date.today()
# lista = ['넷', '셋', '둘']
# # f = open('./Data/Test.csv','a', newline='')
# data = {
#     'text' : lista
# }
# path = './Data/test '+str(day)+'.csv'
# frame = pd.DataFrame(data)
# print(frame)
# frame.to_csv(path, encoding='utf-8-sig')


## 채용 사이트 테스터##
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
# import pandas as pd
# #크롬 경로
# options = webdriver.ChromeOptions()
# options.binary_location = "/Users/maria/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"
# #크롬 드라이버 경로
# chrome_driver_binary = "/Users/maria/Desktop/Code/capstone_3/chromedriver"
# driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
#
# url = 'https://programmers.co.kr/job_positions/10813'
# driver.get(url)
# time.sleep(4)
# # data = driver.find_element(by=By.XPATH, value='//*[@id="__next"]/div[3]/div[1]/div[1]/div[1]/div[2]/section/p[2]').text
# # print(f'주요업무 : {data}')
# path = ['/html/body/div[3]/div/div[1]/div/div[1]/section[2]',
#         '/html/body/div[3]/div/div[1]/div/div[1]/section[3]',
#         '/html/body/div[3]/div/div[1]/div/div[1]/section[4]',
#         '/html/body/div[3]/div/div[1]/div/div[1]/section[5]',]
#
# def main():
#     in_data = ''
#     for i in range(0, 3):
#         try:
#             data = driver.find_element(by=By.XPATH, value=path[i]).text
#         except:
#             continue
#         in_data = in_data + data
#
#     data_f = {
#         'text' : []
#     }
#     frame = pd.DataFrame(data_f)
#     frame.loc[0] = in_data
#     # frame.to_csv('test.csv')
#     print(frame)
# if __name__ == '__main__' :
#     main()

# import datetime
#
# d = datetime.date.today()
# print (d)