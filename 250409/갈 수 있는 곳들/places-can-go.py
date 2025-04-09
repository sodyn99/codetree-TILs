from collections import deque

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
starts = [tuple(map(int, input().split())) for _ in range(K)]
visited = [[0 for _ in range(N)] for _ in range(N)]
q = deque()

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y):
    if not is_range(x, y):
        return False
    if visited[x][y] or arr[x][y]:
        return False
    return True

dxs = [-1, 0, 1, 0]
dys = [ 0,-1, 0, 1]
for start in starts:
    x_start, y_start = start[0] - 1, start[1] - 1
    q.append((x_start, y_start))
    visited[x_start][y_start] = 1
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))

s = 0
for v in visited:
    s += sum(v)

print(s)
