n, m = map(int, input().split())

arr = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    arr[x-1][y-1] += 1

for a in arr:
    print(*a)