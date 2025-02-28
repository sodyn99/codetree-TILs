N = int(input())

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]
D = ['E', 'W', 'S', 'N']

x, y = 0, 0
for _ in range(N):
    l, d = input().split()
    d = int(d)
    index = D.index(l)

    x += d * dx[index]
    y += d * dy[index]

print(x, y)
