n = int(input())

for i in range(n):
    for j in range(n):
        if j < i or i == 0 or j == (n - 1):
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()