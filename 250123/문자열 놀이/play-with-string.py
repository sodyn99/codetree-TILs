s, q = input().split()
q = int(q)

for i in range(q):
    Q = input().split()
    Q[0] = int(Q[0])
    s = list(s)
    if Q[0] == 1:
        Q[1], Q[2] = int(Q[1])-1, int(Q[2])-1
        t = s[Q[1]]
        s[Q[1]] = s[Q[2]]
        s[Q[2]] = t
        print(''.join(s))
    else:
        for j in range(len(s)):
            if s[j] == Q[1]:
                s[j] = Q[2]
        print(''.join(s))