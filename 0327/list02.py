scores = [10.0, 9.5, 8.7, 5, 8.2, 8.0]

print(f"제거 전: {scores}")
scores.remove(max(scores))
scores.remove(min(scores))
print(f"제거 후: {scores}")

print(f"평균: {sum(scores)/len(scores)}")