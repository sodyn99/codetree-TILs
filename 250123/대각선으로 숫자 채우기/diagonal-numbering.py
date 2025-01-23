n, m = map(int, input().split())

# Write your code here!
arr = [[0 for _ in range(m)] for _ in range(n)]
c = 0
i, j = 0, 0
ti, tj = 0, 0
while(c < n * m):
    if j < 0 or i >= n:
        if tj >= m - 1:
            tj = m - 1
            ti += 1
        else:
            ti = 0
            tj += 1
        i = ti
        j = tj
    c += 1
    arr[i][j] = c
    i += 1
    j -= 1

for a in arr:
    print(*a)