n = list(map(int, input().split()))
A = list(map(int, input().split()))
B = list(map(int, input().split()))

arr = []

for i in range(n[0]):
    x = "Yes"
    for j in range(n[1]):
        if i + j > n[0]:
            x = "No"
            break
        if A[i + j] != B[j]:
            x = "No"
            break
    arr.append(x)

if "Yes" in arr:
    print("Yes")
else:
    print("No")