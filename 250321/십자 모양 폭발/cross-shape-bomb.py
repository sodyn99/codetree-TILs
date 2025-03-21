N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]
r, c = map(int, input().split())

def is_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

dxs, dys = [0, 1, 0, -1, 0], [0, 0, 1, 0, -1]
for i in range(arr[r-1][c-1]):
    for dx, dy in zip(dxs, dys):
        if is_range(r+dx*i, c+dy*i):
            arr[r+dx*i-1][c+dy*i-1] = 0

ans = []     
for i in range(N):
    tmp = []
    for j in range(N):
        if arr[j][i] == 0:
            continue
        else:
            tmp.append(arr[j][i])
    tmp = [0] * (N - len(tmp)) + tmp
    ans.append(tmp)

for i in range(N):
    for j in range(N):
        print(ans[j][i], end=" ")
    print()