n = int(input())
a = input().split()

A = "".join(a)

i = 1
while i <= len(A):
    print(A[i - 1], end="")
    if i % 5 == 0:
        print()
    i += 1