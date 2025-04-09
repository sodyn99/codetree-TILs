from collections import deque

N, K = map(int, input().split()) # N: 격자 크기, K: 반복 횟수
arr = [list(map(int, input().split())) for _ in range(N)]
def remap(i):
    return int(i) - 1
start = tuple(map(remap, input().split()))
visited = [[0 for _ in range(N)] for _ in range(N)]
q = deque()

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

def can_go(x, y, target):
    if not is_range(x, y):
        return False
    if visited[x][y] or arr[x][y] >= target:
        return False
    return True

def bfs():
    global start
    q.append(start)
    max_num = 0
    while q:
        dxs = [-1, 0, 1, 0]
        dys = [ 0, 1, 0,-1]
        x, y = q.popleft()
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            if can_go(nx, ny, arr[start[0]][start[1]]):
                visited[nx][ny] = 1
                if (nx, ny) not in q:
                    q.append((nx, ny))
                if arr[nx][ny] > max_num and (nx, ny) != start:
                    max_num = arr[nx][ny]
    return max_num

for _ in range(K):
    for i in range(N):
        for j in range(N):
            visited[i][j] = 0
    
    max_num = bfs()
    
    next_x, next_y = N-1, N-1
    for i in range(N):
        for j in range(N):
            if visited[i][j] and arr[i][j] == max_num:
                (next_x, next_y) = min((next_x, next_y), (i, j), key=lambda x: (x[0], x[1]))
    
    if max_num == 0:
        break
    start = (next_x, next_y)

print(start[0]+1, start[1]+1)
                