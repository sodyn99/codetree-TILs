n = int(input())
price = list(map(int, input().split()))

# Write your code here!
M = 0
for i in range(n):
    for j in price[i+1:]:
        if j - price[i] > M:
            M = j - price[i]
print(M)