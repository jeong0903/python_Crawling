import requests
from bs4 import BeautifulSoup
import pyautogui

keyword = pyautogui.prompt("검색어를 입력하세요.")
lastpage = int(pyautogui.prompt("마지막 페이지 번호를 입력해주세요"))
print(f"검색어 : {keyword}")
pageNum = 1
for i in range(1, lastpage * 10, 10):      # 1~10, 11~20, 21~30, (31은 x)
    print(f"\n{pageNum} 페이지 입니다. ")
    response = requests.get(f"https://search.naver.com/search.naver?sm=tab_hty.top&where=news&query={keyword}&start={i}")
    html = response.text
    soup = BeautifulSoup(html, 'html.parser')
    links = soup.select('.news_tit')
    for link in links:
        title = link.text
        url = link.attrs['href']
        print(title, url)
    pageNum = pageNum + 1