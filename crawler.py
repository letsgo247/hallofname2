###그냥 평범하게 가져온거

import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from crawler.models import 임시사전

import re
p = re.compile(r'.+?(?=\()')


for i in range(3,143):
    def crawler():
        req = requests.get('http://haruharudesign.tistory.com/1')
        html = req.text
        soup = BeautifulSoup(html, 'html.parser')
        datas = soup.select('#content > article > section.article > div > center > table > tbody > tr:nth-of-type(%d) > td:nth-child(1) > font' % i)
        dict = []

        for data in datas:
            try:
                dict.append(p.search(data.text).group())
                # print(p.search(data.text).group())
            except:
                pass

        return dict


    if __name__=='__main__':

        temp_dict = crawler()
        for data in temp_dict:
            임시사전(단어=data).save()
