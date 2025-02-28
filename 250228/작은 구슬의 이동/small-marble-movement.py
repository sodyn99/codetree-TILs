N, T = map(int, input().split())
R, C, D = input().split()

arr = [[0 for _ in range(N)] for _ in range(N)]
d_num = {'R': 0, 'D': 1, 'U': 2, 'L': 3}
d_num = d_num[D]
dx, dy = [1, 0, 0, -1], [0, 1, -1, 0]

def is_range(x, y):
    return 0 < x <= N and 0 < y <= N

x, y = int(C), int(R)
t = 0
for _ in range(T):
    nx = x + dx[d_num]
    ny = y + dy[d_num]
    if not is_range(nx, ny):
        d_num = 3 - d_num
    else:
        x, y = nx, ny
    
print(y, x)