N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

def is_range(x, y):
    return 0 <= x < 4 and 0 <= y < 4

x, y = 0, 0
cnt = 0
for i in range(N):
    for j in range(N):
        tmp = 0
        for k in range(4):
            x = j + dx[k]
            y = i + dy[k]
            if is_range(x, y) and arr[x][y] == 1:
                tmp += 1
        if tmp >= 3:
            cnt += 1

print(cnt)