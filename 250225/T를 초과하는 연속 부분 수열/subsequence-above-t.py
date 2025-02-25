n, t = map(int, input().split())
arr = list(map(int, input().split()))

# Write your code here!

m = 0
l = 0
for i in range(n):
    if arr[i] <= t:
        l = 0
    else:
        l += 1
    m = max(m, l)

print(m)