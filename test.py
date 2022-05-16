# from bs4 import BeautifulSoup
# import re
# import time
# from selenium import webdriver
# import feedparser
# import pandas as pd
# import datetime
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
#     url = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=developer&page=1&category=1&divpage=5'
#     url_add = 'https://www.ppomppu.co.kr/zboard/'
#
#     driver.get(url)
#     driver.implicitly_wait(10)
#     htmls = driver.page_source
#     soup = BeautifulSoup(htmls, 'html.parser')
#     href = soup.select('#revolution_main_table > tbody')
#     href = re.findall('href="(.+?)">', str(href))
#     href = url_add+href[3]
#     # href = set(href)
#     # href = list(href)
#     print(href)
# #https://www.ppomppu.co.kr/zboard/view.php?id=developer&page=1&divpage=5&category=1&no=25322
# #https://www.ppomppu.co.kr/zboard/view.php?id=developer&amp;page=1&amp;divpage=5&amp;category=1&amp;no=25322

a, b = map(int, input().split())
print(a+b)
# from bs4 import BeautifulSoup
# import requests
# import re
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
# def month(day_data):
#     month_data = re.search('-(.+?)-', day_data)
#     month_data = month_data.group(1)
#     return month_data
#
# #193
# url = 'https://www.ppomppu.co.kr/zboard/zboard.php?id=developer&page=1&category=1&divpage=5'
# urls = 'https://kldp.org'
# red = requests.get(url)
# soup = BeautifulSoup(red.content, 'html.parser')#revolution_main_table > tbody > tr:nth-child(6) > td:nth-child(3)#revolution_main_table > tbody > tr:nth-child(6) > td:nth-child(3) > a')
# # data = urls+data
# # data = preprocessing(data)
# print(data)
# import pyautogui as p
# # p.press()
#
