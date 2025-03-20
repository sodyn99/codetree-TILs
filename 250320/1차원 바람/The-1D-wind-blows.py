N, M, Q = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

winds = []
for _ in range(Q):
    l, d = input().split()
    l = int(l)
    winds.append([l, d])

def push(a, d):
    if d == 'L':
        a = [a[-1]] + a[:M-1]
        d = 'R'
    else:
        a = a[1:] + [a[0]]
        d = 'L'
    return a, d

def decision(a, b):
    for i in range(M):
        if a[i] == b[i]:
            return True
    return False


for w in winds:
    l, d = w[0]-1, w[1]
    arr[l], d = push(arr[l], d)
    d_up, d_down = d, d
    for l_up in range(l-1, -1, -1):
        if decision(arr[l_up], arr[l_up+1]):
            arr[l_up], d_up = push(arr[l_up], d_up)
        else:
            break
    for l_down in range(l+1, N):
        if decision(arr[l_down], arr[l_down-1]):
            arr[l_down], d_down = push(arr[l_down], d_down)
        else:
            break

for a in arr:
    print(*a)