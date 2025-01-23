a = input()
b = input()

c = 0
for _ in range(len(a)):
    f = a.find(b)
    if f != -1:
        c += 1
        a = a[f+1:]

print(c)