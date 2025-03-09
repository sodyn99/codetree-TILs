N, T = map(int, input().split())
arr = list(map(int, input().split())) + list(map(int, input().split()))

arr = arr[2*N-(T%(2*N)):] + arr[:2*N-(T%(2*N))]

print(" ".join(map(str, arr[:N])))
print(" ".join(map(str, arr[N:])))