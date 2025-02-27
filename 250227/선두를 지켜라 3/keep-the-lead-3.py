N, M = map(int, input().split())
A = [tuple(map(int, input().split())) for _ in range(N)]
B = [tuple(map(int, input().split())) for _ in range(M)]

p_A, p_B = [0], [0]
for a in A:
    for t in range(a[1]):
        p_A.append(p_A[-1] + a[0])
for b in B:
    for t in range(b[1]):
        p_B.append(p_B[-1] + b[0])

prize = []
max_d = 0
for i in range(len(p_A)):
    max_d = max(p_A[i], p_B[i])
    if p_A[i] == max_d and p_B[i] == max_d:
        prize.append(0)
    elif p_A[i] == max_d:
        prize.append(1)
    elif p_B[i] == max_d:
        prize.append(2)
    
changed = 0
for i in range(1, len(prize)):
    if prize[i] != prize[i-1]:
        changed += 1

print(changed)