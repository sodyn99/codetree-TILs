N, M = map(int, input().split())

arr = [[0 for _ in range(M)] for _ in range(N)]
dx, dy = [0, 1, 0, -1], [1, 0, -1, 0]

def is_range(x, y):
    return 0 <= x < N and 0 <= y < M

t = 0
x, y = 0, 0
direction = 0
for _ in range(N * M):
    t += 1
    arr[x][y] = t
    nx, ny = x + dx[direction], y + dy[direction]
    if is_range(nx, ny):
        if arr[nx][ny] == 0:
            x, y = nx, ny
        else:
            direction += 1
            direction = direction % 4
            x += dx[direction]
            y += dy[direction]
    else:
        direction += 1
        direction = direction % 4
        x += dx[direction]
        y += dy[direction]

for a in arr:
    print(*a)