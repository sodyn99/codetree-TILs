n = int(input())
arr = list(map(int, input().split()))

# Write your code here!

sum_arr = [0 for _ in range(len(arr))]
for i in range(len(arr)):
    if i == 0:
        max_sum = arr[i]
    else:
        max_sum = max(arr[i], max_sum + arr[i])
    sum_arr[i] = max_sum

print(sum_arr)
print(max(sum_arr))
