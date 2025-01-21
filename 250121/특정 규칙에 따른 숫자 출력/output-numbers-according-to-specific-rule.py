n = int(input())

c = 0
for i in range(n):
    for j in range(n):
        if j < i:
            print(" ", end=" ")
        else:
            c += 1
            print(c, end=" ")
            if c == 9:
                c = 0
    print()