a = list(input())

for i in range(len(a)):
    if ord(a[i]) > 90:
        a[i] = a[i].upper()
    else:
        a[i] = a[i].lower()
print(''.join(a))