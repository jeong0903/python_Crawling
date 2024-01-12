import requests
from bs4 import BeautifulSoup

response = requests.get("https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query=%EA%B0%9C%EB%B0%9C%EC%9E%90+%EC%B1%84%EC%9A%A9&oquery=%EA%B0%9C%EB%B0%9C%EC%9E%90&tqi=iju1Bwqo1LwssKe%2FEhVssssstXw-180010")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
links = soup.select('.news_tit')
for link in links:
    title = link.text
    url = link.attrs['href']
    print(title, url)