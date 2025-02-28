N, T = map(int, input().split())
R, C, D = input().split()

arr = [[0 for _ in range(N)] for _ in range(N)]
d_num = {'R': 0, 'D': 1, 'U': 2, 'L': 3}
d_num = d_num[D]
dx, dy = [1, 0, 0, -1], [0, -1, 1, 0]

def is_range(x, y):
    return 0 <= x < N and 0 <= y < N

x, y = int(C) - 1, int(R) - 1
t = 0
while t < T:
    if not is_range(x, y):
        d_num = 3 - d_num
        x += dx[d_num]
        y += dy[d_num]
    else:
        t += 1
        x += dx[d_num]
        y += dy[d_num]
    
print(y + 1, x + 1)