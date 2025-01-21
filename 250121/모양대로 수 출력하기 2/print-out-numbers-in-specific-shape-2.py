n = int(input())

c = 2
for i in range(n):
    for j in range(n):
        print(c, end=" ")
        c += 2
        if c == 10:
            c = 2
    print()