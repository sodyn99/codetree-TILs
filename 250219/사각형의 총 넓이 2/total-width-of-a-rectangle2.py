n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

offset = abs(min(min(arr)))
size = [[0] * (100 + offset) for _ in range(100 + offset)]
for a in arr:
    for i in range(a[0], a[2]):
        for j in range(a[1], a[3]):
            size[i][j] = 1

print(sum(sum(size, [])))