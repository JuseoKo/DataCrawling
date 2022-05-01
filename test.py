# import bs4
# import requests
# from bs4 import BeautifulSoup
# import re
# import feedparser
# f = feedparser.parse('https://v2.velog.io/rss/tjdrn990423')
# for i in range(0,3):
#     try:
#         print(f.keys())
#         print(f['entries'][0]['summary'])
#     except KeyError:
#         print('예외처리')
#     j = -1
# print('아니 \b 아니\f아니')

# for i in f['entries'] :
#     j = j+1
#     data = f['entries'][j]['summary']
#     data = re.sub('<(.+?)>','', data)
#     data = re.sub('\n', '', data)
#     print(f'데이터 : {data}')

#{'bozo': False,'entries':
# print(f)
# pprint(f.entries[])
# data = re.findall('summary\':(.+?)</p>\',', f)
# data = re.sub('<(.+?)>','', data[0])
# data = re.sub('&quot','', data)
# data = re.sub('(\n)', '', data)
# print(data)
# # print(f['feed']['summary'])
# print(f['feed'].keys())
# data = f['feed']['summary']
# print(f'정보 : {data}')
# for feed in f['feed']:
#     print(feed)

# # Print all title in entries
# for feed in f['entries']:
#     print(feed.updated)

days_list = []
days = 202204
for i in range(0,30):
    if days%100 == 1:
        days = days-89
    else:
        days = days-1
    days_list.append(days)
print(days_list)




# import pandas as pd
#
# #판다스
# data = {
#     'text' : [],
#     'day' : []
# }
# frame = pd.DataFrame(data)
# frame.loc[0, 'day'] = 'ㅇㅇ'
# frame.loc[0, 'text'] = 'ff'
# frame.to_csv('./Data/test.csv', encoding='utf-8-sig')
# print(frame)

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


