surnames = ["kim", "Lee", "Yun"]

for surname in surnames:
    print(surname)

for i in range(3):
    print(i+1)

for index in range(len(surnames)):
    print(index+1, surnames[index])

for index, surname in enumerate(surnames): #동시에 두개의 값을 가지고 오는 함수
    print(index+1, surname)