import re

email = "rookies@example.com"

#() 로 정규표현식 내 그룹 생성
pattern = re.compile("(\w+)@(\w+\.\w+)")

match = pattern.match(email)

if match:
    username = match.group(1)
    domain = match.group(2)
    print(f"사용자 이름: {username}")
    print(f"도메인 주소: {domain}")