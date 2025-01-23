n = int(input())
arr = [[0 for _ in range(n)] for _ in range(n)]

if n % 2 == 0:
    t = 0
else:
    t = 1

c = 0
i, j = n - 1, n - 1
while c < n**2:
    c += 1
    arr[i][j] = c
    if j % 2 == t:
        i += 1
        if i == n:
            i = n - 1
            j -= 1
    else:
        i -= 1
        if i == -1:
            i = 0
            j -= 1

for a in arr:
    print(*a)