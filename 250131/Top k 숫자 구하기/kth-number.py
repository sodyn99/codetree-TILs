n, k = map(int, input().split())
nums = list(map(int, input().split()))

# Write your code here!
nums_sort = sorted(nums)
print(nums_sort[k-1])