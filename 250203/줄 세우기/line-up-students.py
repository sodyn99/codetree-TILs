n = int(input())
students = [tuple(map(int, input().split())) + (i + 1,) for i in range(n)]

# Write your code here!

class Student:
    def __init__(self, height, weight, id):
        self.height = height
        self.weight = weight
        self.id = id

ss = [Student(students[i][0], students[i][1], students[i][2]) for i in range(n)]
ss.sort(key=lambda x: (-x.height, -x.weight, x.id))

for _, s in enumerate(ss):
    print(s.height, s.weight, s.id)