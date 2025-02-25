n = int(input())
arr = [int(input()) for _ in range(n)]

l = 0
m = 1
for i in range(n):
    if i == 0 or arr[i] - arr[i-1] <= 0:
        l = 0
    l += 1
    m = max(m, l)

print(m)