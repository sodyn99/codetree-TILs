import copy

N, M, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
points = [tuple(map(int, input().split())) for _ in range(Q)]

arrF = copy.deepcopy(arr)
def in_range(x, y):
    return 0 <= x < N and 0 <= y < M

def average(arr, x, y):
    dxs, dys = [0, 1, -1, 0, 0], [0, 0, 0, 1, -1]
    s = 0
    c = 0
    for dx, dy in zip(dxs, dys):
        if in_range(x+dx, y+dy):
            s += arr[x+dx][y+dy]
            c += 1
    return int(s / c)

for q in range(Q):
    x1, y1, x2, y2 = points[q]
    x1 -= 1
    y1 -= 1
    x2 -= 1
    y2 -= 1

    arr = copy.deepcopy(arrF)
    
    tmp = [arr[x1+1][y1], arr[x1][y2-1], arr[x2][y1+1], arr[x2-1][y2]]

    for i in range(y1+1, y2+1):
        arrF[x1][i] = arr[x1][i-1]
        arrF[x1][y1] = tmp[0]
    for i in range(x1, x2):
        arrF[i][y1] = arr[i+1][y1]
        arrF[x2][y1] = tmp[3]
    for i in range(y1, y2):
        arrF[x2][i] = arr[x2][i+1]
        arrF[x2][y2] = tmp[2]
    for i in range(x1, x2+1):
        arrF[i][y2] = arr[i-1][y2]
        arrF[x1][y2] = tmp[1]

    arr = copy.deepcopy(arrF)

    for i in range(x1, x2+1):
        for j in range(y1, y2+1):
            arrF[i][j] = average(arr, i, j)

for a in arrF:
    print(*a)