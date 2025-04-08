N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y):
    if not is_range(x, y):
        return False
    if visited[x][y] == 1:
        return False
    if field[x][y] == 0:
        return False
    return True

def dfs(x, y):
    global cnt
    visited[x][y] = 1
    cnt += 1
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny):
            dfs(nx, ny)
    return cnt

villages = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if can_go(i, j):
            villages.append(dfs(i, j))

new_villages = []
for v in villages:
    if v > 0:
        new_villages.append(v)

new_villages.sort()
print(len(new_villages))
for v in new_villages:
    print(v)