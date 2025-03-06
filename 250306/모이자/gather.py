orders = list(input())

x, y = 0, 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
direction = 3
for order in orders:
    if order == 'L':
        direction = (direction - 1 + 4) % 4
    elif order == 'R':
        direction = (direction + 1) % 4
    else:
        x += dx[direction]
        y += dy[direction]

print(x, y)