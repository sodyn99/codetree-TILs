n = int(input())
name = []
street_address = []
region = []

for _ in range(n):
    n_i, s_i, r_i = input().split()
    name.append(n_i)
    street_address.append(s_i)
    region.append(r_i)

# Write your code here!

class Location:
    def __init__(self, name, address, region):
        self.name = name
        self.address = address
        self.region = region
    
    def print_location(self):
        print("name", self.name)
        print("addr", self.address)
        print("city", self.region)

locations = [Location(name[i], street_address[i], region[i]) for i in range(n)]
locations.sort(key=lambda x: x.name)
locations[-1].print_location()