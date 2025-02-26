N = int(input())

arr = [0 for _ in range(1000)]
t = 0
for _ in range(N):
    x, D = input().split()
    x = int(x)
    t0 = t
    if D == 'R':
        t += x
    else:
        t -= x
    for i in range(min(t0, t), max(t0, t)):
        arr[i] += 1

s = 0
for a in arr:
    if a >= 2:
        s += 1

print(s)