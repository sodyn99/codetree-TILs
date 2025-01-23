A = input()
B = input()

# Write your code here!
t = 1
while t > 0:
    t = A.find(B)
    A = list(A)
    A = A[:t] + A[t+len(B):]
    A = ''.join(A)
print(A)