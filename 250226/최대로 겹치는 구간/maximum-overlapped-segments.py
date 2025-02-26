n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr = [0] * (max(max(segments)) + 100)
for i in range(n):
    for j in range(segments[i][0]+99, segments[i][1]+99):
        arr[j] += 1

print(max(arr))