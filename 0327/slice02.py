STUDENT = 5
scores = []
count = 0

for i in range(STUDENT):
    value = int(input(f"학생{i+1}의 성적: "))
    scores.append(value)
    if value >= 80:
        count = count + 1


print(f"최대 점수: {max(scores)}")
print(f"최소 점수: {min(scores)}")
print(f"평균 점수: {sum(scores)/len(scores)}")
print(f"80점 이상은 {count}명입니다.")
