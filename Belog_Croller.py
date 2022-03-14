import requests
from bs4 import BeautifulSoup

# 벨로그 크롤링

# 주소값
url = 'https://velog.io/'
#객체준비와 한글깨짐을 방지하기 위해 인코딩
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser', from_encoding='cp949')

href_list = [] #크롤링한 주소를 담아둘 배열

# 25개 게시글
for i in range(0, 24) :
    #  선택 경로안에 있는 href 테그만 25개를 불러옴
    href = soup.select('#root > div.sc-dPiLbb > div.sc-bqiRlB.eeKvZX > div.sc-bBHHxi.iFCgdF > main.sc-cNKqjZ.frPFLP > div.sc-eJwWfJ.hPOjoM > div.sc-jgrJph.fubVJV > a.sc-hUpaCq.keJMFL')[i].get("href")
    # 상대경로를 절대경로로 바꿔줌
    add_href = 'https://velog.io' + href
    #위에 만들어둔 배열에 저장
    href_list.append(add_href)

#결과출력
print(f'벨로그 : {href_list}')
