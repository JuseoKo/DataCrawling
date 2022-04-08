import requests
from bs4 import BeautifulSoup
import re
import feedparser

url = 'https://programmers.co.kr/job'
#url 세팅
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
# soup = re.findall('<(.+?)>', str(soup))
print(soup)
# data = soup.select('#news_body_area')[0].get_text()
# data = re.sub('\[(.+?)\]', '',str(data))
# data = re.sub('※(.+?)지', '',str(data))
# data = re.sub('/(.+?)뉴스1', '',str(data))


