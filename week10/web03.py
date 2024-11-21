import urllib.request
import pandas as pd
from bs4 import BeautifulSoup
import datetime

#print(datetime.datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초"))

shops = []

for i in range(1, 51):
    url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store="
    #print(url)
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')  # 10

    for tr in trs:
        tds = tr.find_all('td')
        shop_name = tds[1].string  # 매장이름
        shop_addr = tds[3].string  # 주소
        shop_phone = tds[5].string  # 전화번호

        shops.append([shop_name]+[shop_addr]+[shop_phone]+[datetime.datetime.now().strftime("%Y년 %m월 %d일 %H시 %M분 %S초")])  # 2d list

#print(shops)
hollys_df = pd.DataFrame(shops, columns=('매장이름', '주소', '전화번호', '일시'))
hollys_df.to_csv('hollys.csv', encoding='cp949', mode='w')