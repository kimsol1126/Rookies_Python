import requests
import re

req = requests.get("http://ipconfig.kr/")
#print(req) 는 상태코드 (ex. 200, 404)출력
#search는 딱 하나만 찾는다.
address = re.search(r'IP Address: (\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})', req.text)[0] #매치된 전체를 저장. [1]로 하면 그룹으로 묶인 IP주소만 저장
print(address)