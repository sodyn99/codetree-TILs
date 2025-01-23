a = []
for _ in range(3):
    a.append(len(input()))

print(max(a) - min(a))