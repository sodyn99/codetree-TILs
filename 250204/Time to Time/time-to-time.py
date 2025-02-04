a, b, c, d = map(int, input().split())

# Write your code here!

t = 0
while True:
    if a == c and b == d:
        break
    b += 1
    t += 1
    if b == 60:
        a += 1
        b = 0

print(t)
