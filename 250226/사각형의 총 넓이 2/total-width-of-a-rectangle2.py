n = int(input())
x1, y1, x2, y2 = [], [], [], []
for _ in range(n):
    a, b, c, d = map(int, input().split())
    x1.append(a)
    y1.append(b)
    x2.append(c)
    y2.append(d)

# Please write your code here.

arr = [[0 for _ in range(200)] for _ in range(200)]

for k in range(n):
    for i in range(x1[k] + 100, x2[k] + 100):
        for j in range(y1[k] + 100, y2[k] + 100):
            arr[i][j] = 1

area = 0
for a in arr:
    area += sum(a)

print(area)