n, m = map(int, input().split())

arr = [
    [j * m + i + 1 for i in range(m)] for j in range(n)
]

for i in arr:
    print(" ".join(map(str, i)))