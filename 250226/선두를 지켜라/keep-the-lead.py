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

leader, t = 0, 0
for i in range(1, len(d_A)):
    if d_A[i] > d_B[i]:
        if leader == 2:
            t += 1
        leader = 1
    elif d_B[i] > d_A[i]:
        if leader == 1:
            t += 1
        leader = 2

print(t)