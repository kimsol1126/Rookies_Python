from bs4 import BeautifulSoup
import requests

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220615"

headers = {
'User-Agent': 'Mozilla/5.0',
'Content-Type': 'text/html; charset=utf-8'
}

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "lxml")

# print(soup.find_all('div', 'tit5'))
for i in range(len(soup.find_all('div','tit5'))):
    #div → tit5 → a
    print(soup.find_all('div', 'tit5')[i].a.string)
    #td → point
    print(soup.find_all('td', 'point')[i].string)
