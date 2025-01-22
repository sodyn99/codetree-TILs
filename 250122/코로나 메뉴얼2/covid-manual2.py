c = [0] * 4

for i in range(3):
    s, t = input().split()
    t = int(t)
    if s == "Y" and t >= 37:
        c[0] += 1
    elif s == "N" and t >= 37:
        c[1] += 1
    elif s == "Y":
        c[2] += 1
    else:
        c[3] += 1

for i in c:
    print(i, end=" ")

if c[0] >= 2:
    print("E")