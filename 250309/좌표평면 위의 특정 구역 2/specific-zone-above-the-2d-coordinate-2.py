N = int(input())
points = [tuple(map(int, input().split())) for _ in range(N)]

def area(arr):
    min_x, max_x = 40000, 0
    min_y, max_y = 40000, 0
    for a in arr:
        min_x, max_x = min(min_x, a[0]), max(max_x ,a[0])
        min_y, max_y = min(min_y, a[1]), max(max_y ,a[1])
    return (max_x - min_x) * (max_y - min_y)

min_area = 1600000000
tmp = points.copy()
for i in range(len(points)):
    del tmp[i]
    min_area = min(min_area, area(tmp))
    tmp = points.copy()

print(min_area)