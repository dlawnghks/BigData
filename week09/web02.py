import urllib.request
import pandas as pd
from bs4 import BeautifulSoup

shops = []

for i in range(1, 50):
    url = f"https://www.hollys.co.kr/store/korea/korStore2.do?pageNo={i}&sido=&gugun=&store="
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    tbody = soup.find('tbody')
    trs = tbody.find_all('tr')

    for tr in trs:
        tds = tr.find_all('td')
        shop_name = tds[1].string
        shop_adress = tds[3].string
        shop_phone = tds[5].string

        shops.append([shop_name]+[shop_adress]+[shop_phone])

hollys_df = pd.DataFrame(shops, columns=('매장 이름', '주소', '전화번호'))
hollys_df.to_csv('hollys.csv', mode='w')