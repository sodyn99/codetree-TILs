import sys
input = sys.stdin.readline

K, N = map(int, input().split())

rs = []
chk = [False] * (K+1)

def choose(n):
    if n == N:
        print(' '.join(map(str, rs)))
        return
    for i in range(1, K+1):
        rs.append(i)
        choose(n+1)
        rs.pop()
    return
choose(0)
