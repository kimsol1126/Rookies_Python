width = float(input("사각형의 가로 길이를 입력하세요: "))
height = float(input("사각형의 세로 길이를 입력하세요: "))

area = width * height
perimeter = 2 * (width + height)

print(f"사각형의 넓이는 {area:.3f} 이고, 둘레는 {perimeter:.3f} 입니다.")
