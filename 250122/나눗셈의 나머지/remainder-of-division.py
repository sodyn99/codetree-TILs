a, b = map(int, input().split())

c = [0] * b
while(1):
    if a <= 1:
        break
    c[a % b] += 1
    a = a // b

print(sum([i**2 for i in c]))