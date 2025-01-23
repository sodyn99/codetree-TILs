n = int(input())
arr = [
    [1 for _ in range(n)]
] + [
    [1] +
    [0 for _ in range(n-1)] for _ in range(n -1)
]

for i in range(1, n):
    for j in range(1, n):
        arr[i][j] = arr[i][j-1] + arr[i-1][j] + arr[i-1][j-1]
    
for a in arr:
    print(*a)