N = int(input())

direction = {'W': (-1, 0), 'S': (0, -1), 'N': (0, 1), 'E': (1, 0)}
x, y = 0, 0
for _ in range(N):
    d, l = input().split()
    x += direction[d][0] * int(l)
    y += direction[d][1] * int(l)

print(x, y)