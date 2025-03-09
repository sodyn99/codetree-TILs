N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

ans = 0
for i in range(N-2):
    for j in range(N-2):
        coins = 0
        for k in range(3):
            coins += arr[j+k][i] + arr[j+k][i+1] + arr[j+k][i+2]
        ans = max(ans, coins)

print(ans)