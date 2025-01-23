A = input()
B = input()

# Write your code here!
t = 1
if B in A:
    while t > 0:
        t = A.find(B)
        A = list(A)
        A = A[:t] + A[t+len(B):]
        A = ''.join(A)
print(A)