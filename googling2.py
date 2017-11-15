import requests
from bs4 import BeautifulSoup


import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()


이름='이름1'

req = requests.get('https://www.google.com/search?tbm=isch&q="이름1"')
html = req.text
soup = BeautifulSoup(html, 'html.parser')
datas = soup.select('div > a > img')
print(soup)
#rg_s > div:nth-child(1) > a > img
#rg_s > div:nth-child(2) > a > img


# for i in range(3,143):
#     def crawler():
#         req = requests.get('http://haruharudesign.tistory.com/1')
#         html = req.text
#         soup = BeautifulSoup(html, 'html.parser')
#         datas = soup.select('#content > article > section.article > div > center > table > tbody > tr:nth-of-type(%d) > td:nth-child(1) > font' % i)
#         dict = []
#
#         for data in datas:
#             try:
#                 dict.append(p.search(data.text).group())
#                 # print(p.search(data.text).group())
#             except:
#                 pass
#
#         return dict
#
#
#     if __name__=='__main__':
#
#         temp_dict = crawler()
#         for data in temp_dict:
#             임시사전(단어=data).save()
