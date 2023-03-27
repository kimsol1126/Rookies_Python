menu = 0
friends = ["지수","예림","영준"]
index = 0

while menu != 9:
    print("--------------------")
    print("1. 친구 리스트 출력")
    print("2. 친구 추가")
    print("3. 친구 삭제")
    print("4. 친구 이름 변경")
    print("5. 종료")
    print("--------------------")

    button = int(input("원하시는 번호를 선택하세요. "))

    if button == 1:
        print(friends)
    elif button == 2:
        friends.append(input("추가할 친구의 이름을 입력하세요. "))
        print("추가가 완료되었습니다.")
    elif button == 3:
        friends.remove(input("삭제할 친구의 이름을 입력하세요. "))
        print("삭제가 완료되었습니다.")
    elif button == 4:
        update_from = input("이름을 바꿀 친구를 입력하세요. ")
        update_to = input("어떤 이름으로 변경할 지 입력하세요. ")
        for i in range(len(friends)):
            if(friends[i] == update_from):
                friends[i] = update_to
                print("변경이 완료되었습니다.")
    elif button == 5:
        break
    else:
        print("잘못된 번호입니다")


