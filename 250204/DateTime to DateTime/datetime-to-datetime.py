a, b, c = map(int, input().split())

# Write your code here!

t = 0
d, h, m = 11, 11, 11
while True:
    if a <= 11 and b <= 11 and c <= 11:
        print(-1)
        break
    elif d == a and h == b and m == c:
        break
    t += 1
    m += 1
    if m == 60:
        h += 1
        m = 0
    if h == 24:
        d += 1
        h = 0

print(t)