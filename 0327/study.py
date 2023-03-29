guest = {}
button = 0

print("-----------")
print("1. 회원 가입")
print("2. 로그인")
print("3. 회원 아이디 목록 보기")
print("4. 종료")
print("-----------")

while button != 4:
    button = int(input("번호 선택(1~4): "))
    if(button == 1):
        id = input("아이디를 입력해주세요\n")
        pw = input("비밀번호를 입력해주세요\n")
        guest[id] = pw
        print(f"회원가입이 완료되었습니다. 아이디는 {id}이고 패스워드는 {pw}입니다.")
    elif(button == 2):
        id = input("아이디를 입력해주세요\n")
        pw = input("비밀번호를 입력해주세요\n")
        if id in guest:
            if(guest[id] == pw):
                print("로그인 되셨습니다.")
            else:
                while(guest[id] != pw):
                    print("비밀번호가 일치하지 않습니다.")
                    pw = input("비밀번호를 다시 입력해주세요")
                print("로그인 되셨습니다.")
        else:
            print("일치하는 아이디가 없습니다.")
    elif(button == 3):
        for guest_id, guest_pw in guest.items():
            print(f"id : {guest_id} / pw : {guest_pw}")
    elif(button == 4):
        print("프로그램을 종료합니다.")
    else:
        print("버튼을 잘못 누르셨습니다. 다시 선택해주세요. ")


