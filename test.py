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

import pandas as pd
lista = ['하나', '둘', '셋', '넷']
# f = open('./Data/Test.csv','a', newline='')
data = {
    'text' : lista
}
frame = pd.DataFrame(data)
print(frame)
frame.to_csv('./Data/Work1.csv', encoding='utf-8-sig')

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
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
#     print(in_data)
# if __name__ == '__main__' :
#     main()
