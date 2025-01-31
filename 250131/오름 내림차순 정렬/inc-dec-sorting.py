n = int(input())
nums = list(map(int, input().split()))

# Write your code here!
nums.sort()
for n in nums:
    print(n, end=" ")
print()
nums.sort(reverse=True)
for n in nums:
    print(n, end=" ")