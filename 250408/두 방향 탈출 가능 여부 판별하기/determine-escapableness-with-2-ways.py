N, M = map(int, input().split())
room = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
visited[0][0] = 1

def is_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    if not is_range(x, y):
        return False
    if room[x][y] == 0:
        return False
    return True

result = 0
def dfs(x, y):
    global result
    if x == N-1 and y == M-1:
        result = 1
        return

    dxs, dys = [1, 0], [0, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny) and visited[nx][ny] == 0:
            visited[nx][ny] = 1
            dfs(nx, ny)

dfs(0, 0)
print(result)