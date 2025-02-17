n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!

arr = [0 for _ in range(101)]

for i in segments:
    for j in range(i[0], i[1]+1):
        arr[j] += 1

print(arr)
