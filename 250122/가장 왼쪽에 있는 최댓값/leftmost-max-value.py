n = int(input())
a = list(map(int, input().split()))

# Write your code here!
for i in range(n):
    ind = a.index(max(a))
    if ind == 0:
        print(ind + 1, end=" ")
        break
    else:
        print(ind + 1, end=" ")
        a = a[:ind]