n, m = map(int, input().split())

d = []
t = []
for _ in range(n):
    direction, time = input().split()
    d.append(direction)
    t.append(int(time))

d2 = []
t2 = []
for _ in range(m):
    direction, time = input().split()
    d2.append(direction)
    t2.append(int(time))

# Write your code here!

def distance(d, t):
    if d == "R":
        return t
    else:
        return -t

a, b = 0, 0
d += [0 for _ in range(m)]
t += [0 for _ in range(m)]
d2 += [0 for _ in range(n)]
t2 += [0 for _ in range(n)]
meet = False
for i in range(n+m):
    a += distance(d[i], t[i])
    b += distance(d2[i], t2[i])
    # print("-----", a, b)
    if a == b:
        print(a + 1)
        meet = True
        break

if meet == False:
    print(-1)