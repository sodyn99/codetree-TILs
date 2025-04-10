from collections import deque

N, K, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
stones = set()
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            stones.add((i, j))
def initialize_start(i):
    return int(i) - 1
starts = [tuple(map(initialize_start, input().split())) for _ in range(K)]
visited = [[0 for _ in range(N)] for _ in range(N)]

q = deque()

def initialize_visited():
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0

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
def bfs(start):
    q.append(start)
    cnt = 0
    while q:
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                # for v in visited:
                #     print(*v)
                # print("-----------")
                q.append((nx, ny))
                cnt += 1
    return cnt

out = []
def dfs(n):
    global out
    if n == K:
        return
    for stone in stones:
        out.append(stone)
        dfs(n+1)
        out.pop()

print()