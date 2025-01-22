n = int(input())
price = list(map(int, input().split()))

# Write your code here!
arr = []
for i in range(n):
    for j in price[i+1:]:
        arr.append(j - price[i])

if arr != []:
    if max(arr) > 0:
        print(max(arr))
    else:
        print(0)
else:
    print(0)