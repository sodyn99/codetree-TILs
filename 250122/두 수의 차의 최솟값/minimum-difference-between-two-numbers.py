n = int(input())
a = list(map(int, input().split()))

m = a[-1]

for i in range(n):
    for j in a[i+1:]:
        if j - a[i] < m:
            m = j - a[i]

print(m)