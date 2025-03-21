A = list(input())
m = len(A)
for a in range(len(A)):
    tm = 0
    tmp_arr = []
    tmp = 1
    for t in range(1, len(A)):
        if A[t] == A[t-1]:
            tmp += 1
        else:
            tmp_arr.append(len(str(tmp)))
            tm += 1
            tmp = 1
    tm += 1
    tmp_arr.append(len(str(tmp)))
    m = min(m, tm + sum(tmp_arr))
    A = [A[-1]] + A[:len(A)-1]

print(m)