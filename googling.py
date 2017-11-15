from selenium import webdriver
from bs4 import BeautifulSoup

# driver = webdriver.PhantomJS('../Crawler/phantomjs-2.1.1-windows/bin/phantomjs')
driver = webdriver.Chrome('../Crawler/chromedriver')
driver.implicitly_wait(3)

이름 = '안녕하세요'

driver.get('https://www.google.com/search?tbm=isch&q=%s' % 이름)


# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# source = soup.select('tbody > tr > td:nth-of-type(2) > a')
#
# print(source.href)


# driver.get('https://order.pay.naver.com/home')
# html = driver.page_source
# soup = BeautifulSoup(html, 'html.parser')
# notices = soup.select('div.p_inr > div.p_info > a > span')
#
# for n in notices:
#     print(n.text.strip())