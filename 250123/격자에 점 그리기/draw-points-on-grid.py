n, m = map(int, input().split())
arr = [[0 for _ in range(n)] for _ in range(n)]

c = 0
for _ in range(m):
    c += 1
    x, y = map(int, input().split())
    arr[x-1][y-1] = c

for a in arr:
    print(*a)