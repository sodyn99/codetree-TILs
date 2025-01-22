a = [list(map(int, input().split())) for i in range(2)]

print(f"{sum(a[0]) / len(a[0]):.1f} {sum(a[1]) / len(a[1]):.1f}")

for i in range(len(a[0])):
    print(f"{(a[0][i] + a[1][i]) / 2:.1f}", end=" ")
print()
print(f"{(sum(a[0]) + sum(a[1])) / (len(a[0]) + len(a[1])):.1f}")