N, M = map(int, input().split())

A, B = [], []
for _ in range(N):
    A.append(list(map(int, input().split())))
for _ in range(M):
    B.append(list(map(int, input().split())))

d_A, d_B = [0], [0]
for i in range(N):
    for j in range(A[i][1]):
        d_A.append(d_A[-1] + A[i][0])
for i in range(M):
    for j in range(B[i][1]):
        d_B.append(d_B[-1] + B[i][0])

arr = []
for i in range(len(d_A)):
    arr.append(d_A[i] - d_B[i])

t = 0
for i in range(2, len(d_A)-1):
    if arr[i] == 0:
        arr[i] = 1
    if arr[i] * arr[i-1] <= 0:
        t += 1

print(t)