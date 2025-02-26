arr = [[0 for _ in range(2000)] for _ in range(2000)]

def offset(x):
    return int(x) + 1000

for k in range(3):
    x1, y1, x2, y2 = map(offset, input().split())

    for i in range(x1, x2):
        for j in range(y1, y2):
            if k == 2:
                arr[i][j] = 0
            else:
                arr[i][j] = 1

area = 0
for a in arr:
    area += sum(a)

print(area)