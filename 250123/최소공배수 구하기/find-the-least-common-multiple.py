n, m = map(int, input().split())

# Write your code here!
for i in range(1, max(n, m) + 1):
    if min(n,m) * i % max(n,m) == 0:
        print(min(n,m) * i)
        break