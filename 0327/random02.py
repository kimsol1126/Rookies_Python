import random

initial_money = 50
goal = 250
wins= 0

for i in range(100):
    cash = initial_money
    while cash > 0 and cash < goal:
        number = random.randint(1,2)
        if number == 1:
            cash = cash + random.randint(1,10)
        else:
            cash = cash - random.randint(1,10)
    if cash == goal:
        wins = wins + 1

print(f"100번 중에서 {wins}번 성공했습니다.")
