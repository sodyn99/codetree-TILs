N, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(3)]

for t in range(T):
    tmp1, tmp2, tmp3 = [arr[0][-1]], [arr[1][-1]], [arr[2][-1]]
    arr[0] = tmp3 + arr[0][:2]
    arr[1] = tmp1 + arr[1][:2]
    arr[2] = tmp2 + arr[2][:2]

for a in arr:
    print(*a)