import requests
import re

url = "https://sports.v.daum.net/v/20220613185410223"

headers = {
'User-Agent': 'Mozilla/5.0',
'Content-Type': 'text/html; charset=utf-8'
}

req = requests.get(url, headers=headers)
results = re.search(r'[\w\.-]+@[\w\.-]+', req.text)[0]
results_findall = re.findall(r'[\w\.-]+@[\w\.-]+', req.text)
#set으로 중복값 제외
results_findallset = list(set(results_findall))
print(results)
print(results_findall)
print(results_findallset)

