x1 = [0] * 3
y1 = [0] * 3
x2 = [0] * 3
y2 = [0] * 3

x1[0], y1[0], x2[0], y2[0] = map(int, input().split())
x1[1], y1[1], x2[1], y2[1] = map(int, input().split())
x1[2], y1[2], x2[2], y2[2] = map(int, input().split())

# Write your code here!

arr = [[0] * 2001 for _ in range(2001)]

for x in range(x1[0], x2[0]):
    for y in range(y1[0], y2[0]):
        arr[x][y] = 1
for x in range(x1[1], x2[1]):
    for y in range(y1[1], y2[1]):
        arr[x][y] = 1
for x in range(x1[2], x2[2]):
    for y in range(y1[2], y2[2]):
        arr[x][y] = 0

print(sum(sum(arr, [])))