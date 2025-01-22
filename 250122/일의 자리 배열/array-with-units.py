a, b = map(int, input().split())

arr = [a, b]

for i in range(1, 9):
    arr.append((arr[i] + arr[i-1]) % 10)

for i in arr:
    print(i, end=" ")