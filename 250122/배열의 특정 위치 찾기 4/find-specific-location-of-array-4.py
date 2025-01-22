arr = list(map(int, input().split()))

s = 0
c = 0
for i in arr:
    if i == 0:
        break
    if i % 2 == 0:
        s += i
        c += 1

print(c, s)