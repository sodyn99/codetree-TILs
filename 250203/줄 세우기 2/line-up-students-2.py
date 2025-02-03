n = int(input())
s = [
    (h, w, i + 1)
    for i, (h, w) in enumerate([tuple(map(int, input().split())) for _ in range(n)])
]

# Write your code here!

class Student:
    def __init__(self, id, height, weight):
        self.id = id
        self.height = height
        self.weight = weight

students = [Student(s[i][2], s[i][0], s[i][1]) for i in range(n)]

students.sort(key=lambda x: (x.height, -x.weight))

for student in students:
    print(student.height, student.weight, student.id)