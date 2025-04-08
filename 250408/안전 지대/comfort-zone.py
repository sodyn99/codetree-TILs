import sys
sys.setrecursionlimit(2500)

N, M = map(int, input().split())
houses = [list(map(int, input().split())) for _ in range(N)]
visited = [[0 for _ in range(M)] for _ in range(N)]

def is_range(x, y):
    return 0 <= x < N and 0 <= y < M

def can_go(x, y, K):
    if not is_range(x, y):
        return False
    if visited[x][y] or houses[x][y] <= K:
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
ans_k = 0
for k in range(1, 101):
    K = num_of_safe(k)
    for i in range(N):
        for j in range(M):
            visited[i][j] = 0
    if K > max_K:
        max_K, ans_k = K, k
    
print(ans_k, max_K)

