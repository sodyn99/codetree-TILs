n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
x, y = zip(*points)
x, y = list(x), list(y)

# Write your code here!

arr = [[0] * 201 for _ in range(201)]

for k in range(n):
    for i in range(x[k] + 100, x[k] + 108):
        for j in range(y[k] + 100, y[k] + 108):
            arr[i][j] = 1

s = 0
for a in arr:
    s += sum(a)

print(s)