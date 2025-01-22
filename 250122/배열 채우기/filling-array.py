arr = list(map(int, input().split()))

if arr[-1] == 0:
    arr.pop()

for i in arr[::-1]:
    print(i, end=" ")