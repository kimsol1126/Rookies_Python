from bs4 import BeautifulSoup

page = open("test.html").read()

soup = BeautifulSoup(page, "lxml")

links = soup.find_all("a")
print(len(links))

for link in links:
    href = link['href']
    print(f"{link.string} 링크 : {href}")
