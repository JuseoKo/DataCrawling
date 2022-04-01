# from selenium import webdriver
# from selenium.webdriver.common.by import By
# import time
#
# #크롬 위치
#
# options = webdriver.ChromeOptions()
# options.binary_location = "/Users/maria/Desktop/Google Chrome.app/Contents/MacOS/Google Chrome"
#
# #드라이버 위치
# chrome_driver_binary = "/Users/maria/Desktop/Code/capstone_3/chromedriver"
# driver = webdriver.Chrome(chrome_driver_binary, chrome_options=options)
#
# #변수선언
#
#
# #테이블지정
# count = str(1)
# path = '//*[@id="__next"]/div[3]/div/div/div[3]/ul/li['+count+']/div/a'
#
# #url
# driver.get('https://www.wanted.co.kr/wdlist?country=kr&job_sort=job.latest_order&years=-1&locations=all')
# #
# time.sleep(3)
# sss = 10
# for i in range(0 ,sss):
#     driver.execute_script(f"window.scrollTo(0, 1000*{i})")
#     time.sleep(1)
#     print('스크롤 내림')
#
# while True:
#     pass
# # url_data = driver.find_element(by=By.XPATH, value=path).get_attribute('href')
# print(f'주소 : {url_data}')
#---------------------------------------
# from bs4 import BeautifulSoup
# import requests
# url = 'https://www.wanted.co.kr/wd/105105'
# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'html.parser', from_encoding='cp949')
# data = soup.select('#__next > div.JobDetail_cn__WezJh > div.JobDetail_contentWrapper__DQDB6')
#--------
for i in range(0, 5):
    print(i)