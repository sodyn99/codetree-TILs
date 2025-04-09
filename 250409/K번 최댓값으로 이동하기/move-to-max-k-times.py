from collections import deque

N, K = map(int, input().split()) # N: 격자 크기, K: 반복 횟수
arr = [list(map(int, input().split())) for _ in range(N)]
def remap(i):
    return int(i) - 1
start = tuple(map(remap, input().split()))
visited = [[0 for _ in range(N)] for _ in range(N)]
no = [[0 for _ in range(N)] for _ in range(N)]

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y):
    if not is_range(x, y):
        return False
    if visited[x][y] or no[x][y]:
        return False
    return True

def bfs():
    global start
    q = deque([start])
    max_num = 0
    tmp = []
    while q:
        dxs = [-1, 0, 1, 0]
        dys = [ 0, 1, 0,-1]
        x, y = q.popleft()
        for i in range(N):
            for j in range(N):
                if arr[i][j] >= arr[start[0]][start[1]]:
                    no[i][j] = 1
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny):
                visited[nx][ny] = 1
                q.append((nx, ny))
                tmp.append((nx, ny))
                if arr[nx][ny] > max_num and (nx, ny) != start:
                    max_num = arr[nx][ny]

    (next_x, next_y) = (N-1, N-1)
    for tx, ty in tmp:
        if arr[tx][ty] == max_num:
            (next_x, next_y) = min((next_x, next_y), (tx, ty), key=lambda x: (x[0], x[1]))
            # print(max_num, (tx, ty), (next_x, next_y))
    start = (next_x, next_y)

    return next_x, next_y

X, Y = 0, 0
for _ in range(K):
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0
    
    newX, newY = bfs()
    if (newX, newY) == (X, Y):
        break
    X, Y = newX, newY

print(X++1, Y+1)
                