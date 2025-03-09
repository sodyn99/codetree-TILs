N, T = map(int, input().split())
arr = list(map(int, input().split())) + list(map(int, input().split()))

arr = arr[2*N-T:] + arr[:2*N-T]

print(" ".join(map(str, arr[:N])))
print(" ".join(map(str, arr[N:])))

