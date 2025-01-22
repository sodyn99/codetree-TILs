a = [list(map(int, input().split())) for i in range(4)]

s = 0
for i in range(len(a[0])):
    for j in range(len(a)):
        if j <= i:
            s += a[i][j]

print(s)