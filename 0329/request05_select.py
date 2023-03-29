from bs4 import BeautifulSoup
import requests

url = "https://movie.naver.com/movie/sdb/rank/rmovie.naver?sel=cur&date=20220615"

headers = {
'User-Agent': 'Mozilla/5.0',
'Content-Type': 'text/html; charset=utf-8'
}

req = requests.get(url, headers=headers)
soup = BeautifulSoup(req.text, "lxml")

movie_title = soup.select("#old_content > table > tbody > tr > td.title > div > a")
movie_point = soup.select("#old_content > table > tbody > tr > td.point")

for title, point in zip(movie_title, movie_point):
    print(f"영화 제목: {title.string} 평점: {point.string}")