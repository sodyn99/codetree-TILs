start, end = map(int, input().split())

# Write your code here!

c = 0
for i in range(start + 1, end + 1):
    k = 0
    for j in range(1, i):
        if i % j == 0:
            k += j
    if k == i:
        c += 1
print(c)
