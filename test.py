from bs4 import BeautifulSoup
import re
import time
from selenium import webdriver
import feedparser
import pandas as pd
import datetime
import pandas as pd

import re
# def preprocessing(data):
#     data_def = re.sub('<(.+?)>', '',str(data))
#     data_def = re.sub('\r', '', str(data_def))
#     data_def = re.sub('\t', '', str(data_def))
#     data_def = re.sub('\n', '', str(data_def))
#     data_def = re.sub('\f', '', str(data_def))
#     data_def = re.sub('\v', '', str(data_def))
#     data_def = re.sub('\[', '', str(data_def))
#     data_def = re.sub('\]', '', str(data_def))
#     data_def = data_def.strip()
#     return data_def

# f = open('./2.txt', 'r')

# #193
# # url = 'https://gall.dcinside.com/board/view/?id=programming&no=165001'
# url = 'https://www.ppomppu.co.kr/zboard/view.php?id=developer&page=1&divpage=5&no=2'
# urls = 'https://kldp.org'
# red = requests.get(url)
# soup = BeautifulSoup(red.content, 'html.parser').text
# # data = soup.select('body > div > div.contents > div.container > div')
# # data = soup.select('body > div > div.contents > div.container > div > table:nth-child(15) > tbody > tr:nth-child(1) > td > table > tbody > tr > td > table > tbody > tr > td')
# # data = urls+data
# # data = preprocessing(data)
# print(soup)
# import pyautogui as p
# # p.press()

# from bs4 import BeautifulSoup
#
# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import feedparser
# import pandas as pd
# import datetime
#
# #각종 변수선언
# if True:
#     #크롬드라이버 관련
#     #크롬 경로
#     options = webdriver.ChromeOptions()
#     options.binary_location = "/Users/maria/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"
#     #크롬 드라이버 경로
#     chrome_driver_binary = "/Users/maria/Desktop/Code/capstone_3/chromedriver"
#     driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
#
#     #URL 과 RSS 데이터를 몇개 받아올지 갯수
#     url = 'https://www.ppomppu.co.kr/zboard/view.php?id=developer&page=1&divpage=5&no=10000'
#     value = '/html/body/div/div[2]/div[5]/div/table[5]/tbody/tr[1]/td/table/tbody/tr/td/table/tbody/tr/td'
#     value_2 = '/html/body/div/div[2]/div[5]/div/table[2]/tbody/tr[3]/td/table/tbody/tr/td[5]/div/div[1]'
# driver.get(url)
# data = driver.find_element(by=By.XPATH, value=value).text
# data = preprocessing(data)
# day = driver.find_element(by=By.XPATH, value=value_2).text
# day = re.search('등록일: (.+?) ', day)
# day = day.group(1)
# #년 계산
# def year(day_data):
#     year_data = re.sub('-(.+?)*', '', day_data)
#     return year_data
# #월계산
# def month(day_data):
#     month_data = re.search('-(.+?)-', day_data)
#     month_data = month_data.group(1)
#     return month_data
#
# print(year(day))
# print(month(day))

# # month(data_2)
# o = pd.read_csv('./New/okky_Data.csv', index_col=0)
# p = pd.read_csv('./New/ppomppu.csv', index_col=0)
# # n = pd.read_csv('./New/News_Data.csv', index_col=0)
# print(o)


data = 3
print(type(data))