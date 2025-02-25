n = int(input())
arr = [int(input()) for _ in range(n)]

# Write your code here!
m = 1
t = 0
for i in range(n):
    if i == 0 or arr[i] != arr[i-1]:
        t = 0
    t += 1
    m = max(m, t)

print(m)