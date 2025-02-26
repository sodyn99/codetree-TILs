N = int(input())

arr = [0 for _ in range(101)]
for _ in range(N):
    x1, x2 = map(int, input().split())
    for x in range(x1-1, x2):
        arr[x] += 1

print(max(arr))