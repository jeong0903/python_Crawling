import requests
from bs4 import BeautifulSoup

keyword = input("검색어를 입력하세요 >>> ")
response = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=" + keyword)
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit')
for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)