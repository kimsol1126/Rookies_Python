import csv

#example.csv 파일을 csvfile 이란 이름으로 가져오기
with open("example.csv") as csvfile:
    reader = csv.reader(csvfile)
    #헤더정보는 출력에서 제외하고 싶다면 next()
    headers = next(reader)
    for row in reader:
        name, age, gender = row
        print(f"이름: {name}, 나이: {age}, 성별: {gender}")