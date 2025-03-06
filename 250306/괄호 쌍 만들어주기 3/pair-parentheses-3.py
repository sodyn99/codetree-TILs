A = list(input())

s = 0
for i in range(len(A)):
    if A[i] == '(':
        for j in A[i:]:
            if j == ')':
                s += 1

print(s)
