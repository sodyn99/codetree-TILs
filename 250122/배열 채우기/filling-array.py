arr = list(map(int, input().split()))
new = []

for i in range(len(arr)):
    if arr[i] == 0:
        break
    new.append(arr[i])

for i in new[::-1]:
    print(i, end=" ")