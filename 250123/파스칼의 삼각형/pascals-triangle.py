n = int(input())
arr = []

for i in range(1, n+1):
    t = [1 for _ in range(i)]
    arr.append(t)

for i in range(2, n):
    for j in range(1, i):
        arr[i][j] = arr[i-1][j] + arr[i-1][j-1]

for a in arr:
    print(*a)