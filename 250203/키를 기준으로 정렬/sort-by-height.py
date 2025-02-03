n = int(input())
name = []
height = []
weight = []

for _ in range(n):
    n_i, h_i, w_i = input().split()
    name.append(n_i)
    height.append(int(h_i))
    weight.append(int(w_i))

# Write your code here!

class Tall:
    def __init__(self, name, height, weight):
        self.name = name
        self.height = height
        self.weight = weight

    def print_tall(self):
        print(self.name, self.height, self.weight)

talls = [Tall(name[i], height[i], weight[i]) for i in range(n)]
talls.sort(key=lambda x: x.height)

for tall in talls:
    tall.print_tall()