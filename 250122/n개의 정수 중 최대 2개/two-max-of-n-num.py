n = int(input())
a = list(map(int, input().split()))

# Write your code here!
max1, max2 = max(a[0], a[1]), min(a[0], a[1])
for i in a[2:]:
    if i > max1:
        max2 = max1
        max1 = i
    elif i > max2:
        max2 = i
    
print(max1, max2)