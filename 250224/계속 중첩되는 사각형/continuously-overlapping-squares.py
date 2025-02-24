N = int(input())
rect = [list(map(int, input().split())) for _ in range(N)]

offset = 100
arr = [[0] * 201 for _ in range(201)]
for n in range(N):
    for i in range(rect[n][0] + offset, rect[n][2] + offset):
        for j in range(rect[n][1] + offset, rect[n][3] + offset):
            if (n + 1) % 2 == 1:
                arr[i][j] = 1
            else:
                arr[i][j] = 2

s = 0
for a in arr:
    s += a.count(2)

print(s)