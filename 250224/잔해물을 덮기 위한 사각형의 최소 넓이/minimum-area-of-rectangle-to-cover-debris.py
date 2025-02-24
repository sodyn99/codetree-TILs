x1, y1, x2, y2 = [0] * 2, [0] * 2, [0] * 2, [0] * 2
x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())

# Write your code here!

arr = [[0] * 2001 for _ in range(2001)]
for i in range(x1[0] + 1000, x2[0] + 1000):
    for j in range(y1[0] + 1000, y2[0] + 1000):
        arr[i][j] = 1
for i in range(x1[1] + 1000, x2[1] + 1000):
    for j in range(y1[1] + 1000, y2[1] + 1000):
        arr[i][j] = 2

min_x, min_y, max_x, max_y = 2000, 2000, 0, 0
e = 0
for x in range(0, 2001):
    for y in range(0, 2001):
        if arr[x][y] == 1:
            e = 1
            min_x = min(min_x, x)
            min_y = min(min_y, y)
            max_x = max(max_x, x)
            max_y = max(max_y, y)

if e == 0:
    area = 0
else:
    area = (max_x - min_x + 1) * (max_y - min_y + 1)



print(area)