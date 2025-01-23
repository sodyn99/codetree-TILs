a = list(input())

for i in range(1, len(a)):
    if a[i] == a[1]:
        a[i] = a[0]
print(''.join(a))