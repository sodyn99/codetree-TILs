a, b, c, d = map(int, input().split())

# Please write your code here.

t = 0
while not (a == c and b == d):
    t += 1
    b += 1
    if b == 60:
        a += 1
        b = 0

print(t)