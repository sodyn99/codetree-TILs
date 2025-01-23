a = input()

for i in range(len(a)-1, -1, -1):
    if i % 2 != 0:
        print(a[i], end="")