import urllib.request
import urllib.parse

api = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"

station_id = input("지역코드 : ")  # 전국 108, 수도권 109, 강원 105, 제주 184 ...
values = {'stnId':station_id}
url = api + '?' + urllib.parse.urlencode(values)
# print(url)

urls = urllib.request.urlopen(url).read()
texts = urls.decode('utf-8')
print(texts)

"""
지역코드 : 184
https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp?stnId=184

Process finished with exit code 0
"""