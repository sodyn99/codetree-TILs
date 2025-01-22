n = int(input())
arr = list(map(int, input().split()))

c = 0
for i in range(n):
    if arr[i] == 2:
        arr.pop(i)
        arr.append(0)
        c += 1
    if c == 2:
        print(arr.index(2) + 3)
        break