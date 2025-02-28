N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

x, y = 0, 0
cnt = 0
for i in range(N):
    for j in range(N):
        tmp = 0
        for dx, dy in zip(dxs, dys):
            x = j + dx
            y = i + dy
            if is_range(x, y) and arr[y][x] == 1:
                tmp += 1
        if tmp >= 3:
            cnt += 1

print(cnt)