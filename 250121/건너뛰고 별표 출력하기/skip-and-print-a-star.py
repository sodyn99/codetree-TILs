n = int(input())

for i in range(1, n + 1):
    print("*" * i)
    print()

for i in range(1, n):
    print("*" * (n - i))
    print()