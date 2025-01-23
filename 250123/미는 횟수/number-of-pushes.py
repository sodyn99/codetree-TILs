A, B = [input() for _ in range(2)]
c = 0
for i in range(len(A)):
    t = A[-i:] + A[:len(A)-i]
    if t == B:
        print(i)
        break
    c += 1
if c == len(A):
    print(-1)