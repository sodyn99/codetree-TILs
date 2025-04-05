import sys
import copy
# input = sys.stdin.readline

N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
bombed = [[0 for _ in range(N)] for _ in range(N)]
bombs = [
    [[0, 0], [1, 0], [2, 0], [-1, 0], [-2, 0]],
    [[0, 0], [0, 1], [0, -1], [1, 0], [-1, 0]],
    [[0, 0], [1, 1], [-1, 1], [1, -1], [-1, -1]]
]
loc = []
for i in range(N):
    for j in range(N):
        if arr[i][j] == 1:
            loc.append((i, j))

def is_range(i, j):
    return 0 <= i < N and 0 <= j < N

def calc_area(bombed):
    s = 0
    for b in bombed:
        for j in b:
            if j >= 1:
                s += 1
    return s

area = 0
def dfs(n):
    global area
    if n == len(loc):
        area = max(area, calc_area(bombed))
        return

    for t in range(3):
        x, y = loc[n]
        for dx, dy in bombs[t]:
            nx = x + dx
            ny = y + dy
            if is_range(nx, ny):
                bombed[nx][ny] += 1
        dfs(n+1)
        for dx, dy in bombs[t]:
            nx = x + dx
            ny = y + dy
            if is_range(nx, ny):
                bombed[nx][ny] -= 1

dfs(0)
print(area)