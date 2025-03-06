N = int(input())
houses = list(map(int, input().split()))

arr = []
for i in range(N):
    d = 0
    for j in range(N):
        d += houses[j] * abs(i - j)
    arr.append(d)

print(min(arr))