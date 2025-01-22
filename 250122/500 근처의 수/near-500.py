a = list(map(int, input().split()))

M = min(a)
m = max(a)

for i in a:
    if i > 500:
        if i < m:
            m = i
    else:
        if i > M:
            M = i

print(M, m)