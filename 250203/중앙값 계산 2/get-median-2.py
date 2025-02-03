n = int(input())
arr = list(map(int, input().split()))

# Write your code here!
M = []
for i in range(len(arr)):
    if i % 2 == 0:
        a = arr[:i+1]
        mid = sorted(a)[int((len(a)-1)/2)]
        M.append(mid)
print(*M)