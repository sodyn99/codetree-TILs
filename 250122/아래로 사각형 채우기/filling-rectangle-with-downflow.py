n = int(input())

arr = [
    [n * j + i + 1 for j in range(n)] for i in range(n)
]

for a in arr:
    print(*a)