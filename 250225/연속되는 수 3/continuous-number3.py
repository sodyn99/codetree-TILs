N = int(input())
arr = [int(input()) for _ in range(N)]

# Write your code here!

l = 0
m = 1
for i in range(N):
    if i == 0 or arr[i] * arr[i-1] < 0:
        l = 0
    l += 1
    m = max(m, l)
print(m)