N = int(input())
ans = 0
seq = []

def is_beautiful():
    i = 0
    while i < N:
        if i + seq[i] - 1 >= N:
            return False
        for j in range(i, i+seq[i]):
            if seq[j] != seq[i]:
                return False
        i += seq[i]
    return True

def dfs(n):
    global ans
    if n == N:
        if is_beautiful():
            ans += 1
        return
    for j in range(1, 5):
        seq.append(j)
        dfs(n+1)
        seq.pop()

dfs(0)
print(ans)