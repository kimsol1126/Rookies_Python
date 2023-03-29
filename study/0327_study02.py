#딕셔너리 대신 zip 사용 버전

id = []
pw = []

def main():
    print("-----------")
    print("1. 회원 가입")
    print("2. 로그인")
    print("3. 회원 아이디 목록 보기")
    print("4. 종료")
    print("-----------")

    button = 0

    while button != 4:
        button = int(input("번호 선택(1~4): "))
        if(button == 1):
            new_id = input("아이디를 입력해주세요\n")
            while(new_id in id):
                print("동일한 아이디가 있습니다.")
                new_id = input("아이디를 입력해주세요.\n")
            new_pw = input("비밀번호를 입력해주세요\n")
            id.append(new_id)
            pw.append(new_pw)
            print(f"회원가입이 완료되었습니다. 아이디는 {new_id}이고 패스워드는 {new_pw}입니다.")
        elif(button == 2):
            login_id = input("아이디를 입력해주세요\n")
            login_pw = input("비밀번호를 입력해주세요\n")
            
            if(login_id in id):
                if(login_pw == pw[id.index(login_id)]):
                    print("로그인 되셨습니다.")
                else:
                    while(login_pw != pw[id.index(login_id)]):
                        print("비밀번호가 일치하지 않습니다.")
                        login_pw = input("비밀번호를 다시 입력해주세요")
                    print("로그인 되셨습니다.")
            else:
                print("일치하는 아이디가 없습니다.")
        elif(button == 3):
            for guest_id, guest_pw in zip(id, pw):
                print(f"id : {guest_id} / pw : {guest_pw}")
        elif(button == 4):
            print("프로그램을 종료합니다.")
        else:
            print("버튼을 잘못 누르셨습니다. 다시 선택해주세요. ")

main()

