n = 5
name = []
height = []
weight = []

for _ in range(n):
    n, h, w = input().split()
    name.append(n)
    height.append(int(h))
    weight.append(float(w))

# Write your code here!

class PersonalInfo:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

infos = [PersonalInfo(name[i], height[i], weight[i]) for i in range(5)]

print("name")
infos.sort(key=lambda x: x.name)
for info in infos:
    print(info.name, info.height, info.weight)

print()

print("height")
infos.sort(key=lambda x: -x.height)
for info in infos:
    print(info.name, info.height, info.weight)