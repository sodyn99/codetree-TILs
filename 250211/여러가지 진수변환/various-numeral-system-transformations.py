N, B = map(int, input().split())

# Write your code here!
arr = []
while True:
    if N < B:
        arr.append(N)
        break
    arr.append(N%B)
    N //= B

for a in arr[::-1]:
    print(a, end="")