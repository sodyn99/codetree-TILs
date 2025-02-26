A, B, C = map(int, input().split())

d, h, m = 11, 11, 11
t = 0
while not (d == A and h == B and m == C):
    m += 1
    t += 1
    if m == 60:
        m = 0
        h += 1
    if h == 24:
        h = 0
        d += 1

print(t)