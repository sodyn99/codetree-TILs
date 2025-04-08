N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

visited = [[0 for _ in range(N)] for _ in range(N)]
area = 0
cnt = 0

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y, t):
    if not is_range(x, y):
        return False
    if arr[x][y] != t or visited[x][y]:
        return False
    return True

def dfs(x, y, t):
    chk = 0
    global area
    visited[x][y] = 1
    area += 1
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, t):
            dfs(nx, ny, t)
    if area >= 4:
        arr[x][y] = 0
        chk = 1
    return area, chk

max_area = 0
for i in range(N):
    for j in range(N):
        area = 0
        t = arr[i][j]
        if can_go(i, j, t):
            area, chk = dfs(i, j, t)
            max_area = max(max_area, area)
            if chk == 1:
                cnt += 1

print(cnt, max_area)