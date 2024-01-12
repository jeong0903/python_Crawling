import requests
from bs4 import BeautifulSoup

response = requests.get("https://www.inflearn.com/")
html = response.text
soup = BeautifulSoup(html, 'html.parser')
word = soup.select_one('.new-curation-card__title')
print(word.text)