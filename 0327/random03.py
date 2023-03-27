import random

answer = random.randint(1,100)
count = 0

for i in range(10):
    num = int(input("어떤 수인지 맞춰보세요! "))
    count = count + 1

    if(answer > num):
        print("입력한 값보다 큽니다")
        
    elif(answer < num):
        print("입력한 값보다 작습니다")
        
    else:
        print(f"정답입니다! {count}번 만에 맞췄습니다.")
        break