n, m = map(int, input().split())

arr = [[0 for _ in range(m)] for _ in range(n)]

# Write your code here!
for i in range(n):
    for j in range(m):
        if j % 2 == 0:
            arr[i][j] = i + n * j
        else:
            arr[i][j] = n * (j + 1) - i - 1

for a in arr:
    print(*a)
