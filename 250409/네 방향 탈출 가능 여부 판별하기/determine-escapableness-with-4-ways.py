from collections import deque

N, M = map(int, input().split())
snakes = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]
q = deque([(0, 0)])

def is_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y):
    if not is_range(x, y):
        return False
    if snakes[x][y] == 0 or visited[x][y] == 1:
        return False
    return True

dxs = [ 1, 0,-1, 0]
dys = [ 0,-1, 0, 1]

can_out = 0
while q:
    x, y = q.popleft()
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx, ny):
            if (nx, ny) == (N-1, M-1):
                can_out = 1
                break
            visited[nx][ny] = 1
            q.append((nx, ny))

print(can_out)
        