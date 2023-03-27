#딕셔너리
menu = {
    "아메리카노": 2000,
    "카페라떼": 3000,
    "바닐라라떼": 4000,
    "카푸치노": 3500
}

print("=======메뉴=======")
for name, price in menu.items():
    print(f"{name}: {price}원")
print("==================")

selected_menu = input("주문할 메뉴를 선택하세요 ")
money = int(input("돈을 넣어주세요 "))

price = menu.get(selected_menu, 0)
if price == 0:
    print("잘못된 메뉴입니다.")
else:
    change = money - price
    if change >= 0:
        print(f"{selected_menu}를 구매했습니다. 잔돈은 {change}원 입니다.")
    else:
        print("돈이 부족합니다.")