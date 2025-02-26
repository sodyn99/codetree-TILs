n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.

arr = [0] * max(max(segments))
for i in range(n):
    for j in range(segments[i][0], segments[i][1]):
        arr[j] += 1

print(max(arr))