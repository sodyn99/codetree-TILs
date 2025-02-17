n = int(input())
x = []
dir = []
for _ in range(n):
    xi, di = input().split()
    x.append(int(xi))
    dir.append(di)

# Write your code here!

arr = [0 for _ in range(101 + sum(x))]

t = sum(x)
for i in range(n):
    t0 = t
    if dir[i] == 'R':
        t += x[i]
    else:
        t -= x[i]
    for j in range(min(t0, t), max(t0, t)):
        arr[j] += 1

c = 0
for a in arr:
    if a >= 2:
        c += 1

print(c)