import requests
from bs4 import BeautifulSoup

import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

import django
django.setup()

from crawler.models import 임시사전

import re
p = re.compile(r'[a-zA-Z ]+')


for i in range(1043,339,-1):
    req = requests.get('http://www.korean.go.kr/front/foreignSpell/foreignSpellList.do?pageIndex=%d' % i)
    html = req.text
    soup = BeautifulSoup(html, 'html.parser')
    print('page=',i)
    for j in range(10,0,-1):
        한글 = soup.select('table > tbody > tr:nth-of-type(%d) > td:nth-of-type(3)' % j)
        원어 = soup.select('table > tbody > tr:nth-of-type(%d) > td:nth-of-type(2)' % j)

        def 쓸거판단기():
            for w in 원어:
                a = w.text
                try:
                    b = p.search(w.text).group()
                except:
                    return False
                print(a)
                print(b)
                if a == b:
                    print('True')
                    return True
                else:
                    print('False\n')
                    return False


        if __name__=='__main__':
            for i in 한글:
                if 쓸거판단기():
                    임시사전(단어=i.text).save()
                    print('Success!\n')
                else: pass