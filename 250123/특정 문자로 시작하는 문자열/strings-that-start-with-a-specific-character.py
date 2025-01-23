n = int(input())
arr = []

for _ in range(n):
    arr.append(input())

alp = input()

c = 0
l = 0
for i in arr:
    if alp in i:
        c += 1
        l += len(i)

print(c, f"{l/c:.2f}")