arr = list(map(int, input().split()))

s = 0
c = 0
for i in arr:
    if i == 0:
        break
    s += i
    c += 1

print(f"{s} {s/c:.1f}")