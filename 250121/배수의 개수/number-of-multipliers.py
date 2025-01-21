t, f = 0, 0

for i in range(10):
    n = int(input())
    if n % 3 == 0:
        t += 1
    if n % 5 == 0:
        f += 1
print(f"{t} {f}")