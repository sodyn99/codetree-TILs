A = input()
B = input()

# Write your code here!
t = 1
if B in A:
    for _ in range(len(A)):
        t = A.find(B)
        if t < 0:
            break
        A = list(A)
        A = A[:t] + A[t+len(B):]
        A = ''.join(A)
print(A)