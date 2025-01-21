m = int(input())

for i in range(m):
    n = int(input())
    c = 0
    while(1):
        c += 1
        if n % 2 == 0:
            n = n / 2
        else:
            n = n * 3 + 1

        if n == 1:
            break

    print(c)