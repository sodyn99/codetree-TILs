n = int(input())
arr = list(map(float, input().split()))

avg = sum(arr) / n
grade = ""
if avg > 4:
    grade = "Perfect"
elif avg > 3:
    grade = "Good"
else:
    grade = "Poor"

print(round(avg, 1))
print(grade)