import random

options = ["왼쪽", "중앙", "오른쪽"]

#문자열 중 랜덤값 선택은 choice()
choice = random.choice(options)

user = input("패널티킥! 어디를 막을까요? ")

if choice == user:
    print("막았습니다!")
else:
    print("놓쳤습니다! 패널티킥 성공!")

print(f"선수는 {choice}로 찼습니다.")