c = 0
t = []
a = None
while 1:
    a = input()
    if a == "0":
        break
    c += 1
    if c % 2 != 0:
        t.append(a)

print(c)
for i in t:
    print(i)