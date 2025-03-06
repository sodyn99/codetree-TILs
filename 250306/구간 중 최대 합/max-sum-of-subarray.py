N, K = map(int, input().split())
arr = list(map(int, input().split()))

m = 0
for i in range(N-K+1):
    m = max(m, sum(arr[i:i+K]))

print(m)