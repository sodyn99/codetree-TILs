n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Write your code here!

for q in queries:
    a1, a2 = q
    print(sum(arr[a1-1:a2]))