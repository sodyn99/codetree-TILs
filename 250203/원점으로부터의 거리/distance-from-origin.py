n = int(input())
points = [(int(i+1), tuple(map(int, input().split()))) for i in range(n)]

# Write your code here!

class Distance:
    def __init__(self, id, x, y):
        self.id = id
        self.x = x
        self.y = y
    
distances = [Distance(points[i][0], points[i][1][0], points[i][1][1]) for i in range(n)]

distances.sort(key=lambda k: (abs(k.x) + abs(k.y), k.id))

for d in distances:
    print(d.id)