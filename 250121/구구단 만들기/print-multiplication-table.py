a, b = map(int, input().split())

for i in range(1, 10):
    for j in range(b, a-1, -1):
        if j % 2 == 0:
            if j == a or j == a + 1:
                print(f"{j} * {i} = {j * i}", end="")
            else:
                print(f"{j} * {i} = {j * i}", end=" / ")
    print()