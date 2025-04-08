N = int(input())
field = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

def dfs(x, y):
    global cnt
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if is_range(nx, ny) and visited[nx][ny] == 0 and field[nx][ny] == 1:
            visited[nx][ny] = 1
            cnt += 1
            dfs(nx, ny)
    return cnt

villages = []
for i in range(N):
    for j in range(N):
        cnt = 0
        if visited[i][j] == 0:
            villages.append(dfs(i, j))

new_villages = []
for v in villages:
    if v > 0:
        new_villages.append(v)

new_villages.sort()
print(len(new_villages))
for v in new_villages:
    print(v)