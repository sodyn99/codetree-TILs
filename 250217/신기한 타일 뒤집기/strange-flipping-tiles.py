n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)

# Write your code here!

color = [0] * sum(x) * 2

t = sum(x)
for i in range(n):
    step = 1 if dir[i] == 'R' else -1
    t0 = t
    t += step * (x[i] - 1)
    print(t0, t)
    for j in range(t0, t + step, step):
        if t0 > t:
            color[j] = 'white'
        else:
            color[j] = 'black'
print(color)

print(color.count('white'), color.count('black'))
        
