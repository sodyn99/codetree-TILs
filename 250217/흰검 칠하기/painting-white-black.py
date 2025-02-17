n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Write your code here!

color = [0 for _ in range(100 + sum(x))]
white = [0 for _ in range(100 + sum(x))]
black = [0 for _ in range(100 + sum(x))]

t = sum(x)
for i in range(n):
    t0 = t
    if dir[i] == 'R':
        t += x[i] - 1
    else:
        t -= x[i] - 1
    if t0 < t:
        for j in range(t0, t + 1):
            black[j] += 1
            color[j] = 'black'
            if white[j] >= 2 and black[j] >= 2:
                color[j] = 'gray'
    elif t0 == t:
        if dir[i] == 'R':
            for j in range(t0, t + 1):
                black[j] += 1
                color[j] = 'black'
        else:
            for j in range(t0, t - 1, -1):
                white[j] += 1
                color[j] = 'white'
    else:
        for j in range(t0, t - 1, -1):
            white[j] += 1
            color[j] = 'white'
            if white[j] >= 2 and black[j] >= 2:
                color[j] = 'gray'

print(color.count('white'), color.count('black'), color.count('gray'))
