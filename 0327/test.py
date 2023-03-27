name = input("이름을 입력하세요.")
phone = input("전화번호를 입력하새요")
age = input("나이를 입력하세요")
print(type(age))

#print(name,"의 전화번호는", phone, "입니다.", age, "살 입니다.")
print("{}의 전화번호는 {}입니다. 나이는 {} 살입니다.".format(name,phone,age))
print(f"{name}의 전화번호는 {phone} 입니다. 나이는 {age} 살입니다")
print("저장이 완료되었습니다.")
