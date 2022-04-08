# import requests
# from bs4 import BeautifulSoup
# import re
# import feedparser
#
# url = 'https://programmers.co.kr/job'
# #url 세팅
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser')
# # soup = re.findall('<(.+?)>', str(soup))
# print(soup)
# # data = soup.select('#news_body_area')[0].get_text()
# # data = re.sub('\[(.+?)\]', '',str(data))
# # data = re.sub('※(.+?)지', '',str(data))
# # data = re.sub('/(.+?)뉴스1', '',str(data))

# import pandas as pd
# lista = ['하나', '둘', '셋', '넷']
# # f = open('./Data/Test.csv','a', newline='')
# data = {
#     'text' : []
# }
# frame = pd.DataFrame(data)
# print(frame)
# new_text_list = ['다섯', '여섯', '일곱']
#
# frame.lo
# data_count = 0
# for i in range(0, len(new_text_list)) :
#     add_text = new_text_list[i]
#     print(f'데이터 추가: {add_text}')
#     #반환값
#     data_count += 1
#
#     print(data_count)
#     frame.loc[data_count] = add_text
#     print(frame)

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# #크롬 경로
# options = webdriver.ChromeOptions()
# options.binary_location = "/Users/maria/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"
# #크롬 드라이버 경로
# chrome_driver_binary = "/Users/maria/Desktop/Code/capstone_3/chromedriver"
# driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
#
# url = 'https://programmers.co.kr/job_positions/4043'
# driver.get(url)
# data = driver.find_element(by=By.XPATH, value='/html/body/div[3]/div/div[1]/div/div[1]').text
# print(data)

import re
data = '[안녕하세요]'
data = re.sub('\[', '',str(data))
data = re.sub('\]', '',str(data))
print(data)