n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
N = []
for i in nums:
    if nums.count(i) == 1:
        N.append(i)

if N:
    print(max(N))
else:
    print(-1)