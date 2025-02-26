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

A, B = [], []
a, b = 0, 0
meet = False
for i in range(n):
    for j in range(t[i]):
        if d[i] == "R":
            a += 1
        else:
            a -= 1
        A.append(a)
for i in range(m):
    for j in range(t2[i]):
        if d2[i] == "R":
            b += 1
        else:
            b -= 1
        B.append(b)

for i in range(len(A)):
    if A[i] == B[i]:
        meet = True
        print(i + 1)
        break

if meet == False:
    print(-1)