import sys
input = sys.stdin.readline

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]

v = [0 for _ in range(N)]

def corrupt(l1, l2):
    l_first = min(l1, l2)
    l_last = max(l1, l2)
    if l_last[1] <= l_first[1]:
        return True
    return False

cnt = 0
def dfs(n, c):
    global cnt
    if n == N:
        cnt = max(cnt, c)
        return

    for l in range(N):
        if v[l] == 0:
            v[l] = 1
            if corrupt(lines[n], lines[l]):
                dfs(n+1, c)
            else:
                dfs(n+1, c+1)
            v[l] = 0

dfs(0, 0)
print(cnt)