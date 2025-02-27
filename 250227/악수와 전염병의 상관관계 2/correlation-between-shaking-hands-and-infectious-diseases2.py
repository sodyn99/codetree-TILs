N, K, P, T = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(T)]
arr.sort()

developer = [0 for _ in range(N)]
spread = [0 for _ in range(N)]
developer[P-1] = 1

for i in range(T):
    t, x, y = arr[i][0], arr[i][1] - 1, arr[i][2] - 1
    if developer[x] == 1:
        if spread[x] < K:
            developer[y] = 1
            spread[x] += 1
    if developer[y] == 1:
        if spread[y] < K:
            developer[x] = 1
            spread[y] += 1
            
print("".join(list(map(str, developer))))
