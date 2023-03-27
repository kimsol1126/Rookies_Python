menu = {
    "아메리카노": 2000,
    "카페라떼": 3000,
    "바닐라라떼": 4000,
    "카푸치노": 3500
}
order=[]
total = 0

print("=======메뉴=======")
for name, price in menu.items():
    print(f"{name}: {price}원")
print("==================")

while True:
    selected_menu = input("주문할 메뉴를 선택하세요 ")

    if selected_menu == 'q':
        break
    else:
        order.append(selected_menu)
        total = total + menu.get(selected_menu, 0)

price = int(input(f"총 금액은 {total}원 입니다. 돈을 넣어주세요. "))
change = price - total

print(f"{order}를 주문하셨습니다. 잔돈은 {change}원 입니다.")


