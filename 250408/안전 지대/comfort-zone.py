N, M = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

def sink(K):
    sinked = [[0 for _ in range(M)] for _ in range(N)]
    for i in range(N):
        for j in range(M):
            if houses[i][j] <= K:
                sinked[i][j] = 1
    return sinked

def is_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y, K):
    sinked = sink(K)
    if not is_range(x, y):
        return False
    if visited[x][y] or sinked[x][y]:
        return False
    return True

def dfs(x, y, K):
    visited[x][y] = 1
    dxs, dys = [1, 0, -1, 0], [0, 1, 0, -1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if can_go(nx, ny, K):
            dfs(nx, ny, K)

def num_of_safe(K):
    cnt = 0
    for i in range(N):
        for j in range(M):
            if can_go(i, j, K):
                dfs(i, j, K)
                cnt += 1
    return cnt

max_K = 0
Ks = []
for k in range(1, 101):
    K = num_of_safe(k)
    visited = [[0 for _ in range(M)] for _ in range(N)]
    Ks.append(K)
    max_K = max(max_K, K)

for K in range(len(Ks)):
    if Ks[K] == max_K:
        print(K+1, Ks[K])
        break
