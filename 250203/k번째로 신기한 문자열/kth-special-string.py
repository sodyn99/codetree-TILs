n, k, t = input().split()
n, k = int(n), int(k)
str = [input() for _ in range(n)]

# Write your code here!
arr = []
for s in str:
    if t == s[:len(t)]:
        arr.append(s)

arr.sort()

print(arr[k-1])