n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Write your code here!
offset = 0
if min(min(segments)) < 0:
    offset = abs(min(min(segments)))
R = max(max(segments))

arr = [0 for i in range(R)]
for i in range(n):
    for j in range(segments[i][0] + offset, segments[i][1] + offset):
        arr[j] += 1
    
print(max(arr))