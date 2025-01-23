a = list(input())
t = a[1]
for i in range(1, len(a)):
    if a[i] == t:
        a[i] = a[0]
print(''.join(a))