arr = [
    [1 for _ in range(5)]
] + [
    [1, 0, 0, 0, 0] for _ in range(4)
]

for i in range(1, 5):
    for j in range(1, 5):
        arr[i][j] = arr[i-1][j] + arr[i][j-1]

for a in arr:
    print(*a)