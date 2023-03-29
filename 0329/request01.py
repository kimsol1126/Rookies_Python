import requests

url = "https://compphoto.incruit.com/2021/10/SK%EC%89%B4%EB%8D%94%EC%8A%A4_ko.png"

headers = {
'User-Agent': 'Mozilla/5.0',
'Content-Type': 'text/html; charset=utf-8'
}

req = requests.get(url, headers=headers)

#상태코드_Status Good
if req.status_code == 200:
    print("이미지 저장")
    with open("test.png", "wb") as fp:
        fp.write(req.content)