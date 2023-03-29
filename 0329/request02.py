from bs4 import BeautifulSoup

page = open("test.html").read()

soup = BeautifulSoup(page, "lxml")
print(soup.find_all("p", class_="outer-text"))
#class가 명확하게 지정되어 있다면 class만으로도 탐색 가능
print(soup.find_all(class_="outer-text"))
#id 정보를 바탕으로 탐색도 가능
print(soup.find_all(id="first"))
