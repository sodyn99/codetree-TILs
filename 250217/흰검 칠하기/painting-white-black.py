n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Write your code here!

arr = [0 for _ in range(100 + sum(x))]

t = sum(x)
for i in range(n):
    t0 = t
    if dir[i] == 'R':
        t += x[i] - 1
    else:
        t -= x[i] - 1
    for j in range(min(t0, t), max(t0, t) + 1):
        arr[j] += 1

b, g = 0, 0
black = 0
for a in arr:
    if a >= 4:
        g += 1
        if b > 0:
            black = b
        b = 0
    elif a > 0:
        b += 1

print(b, black, g)
    
