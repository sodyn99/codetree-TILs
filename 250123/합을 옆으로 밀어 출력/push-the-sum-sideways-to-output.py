n = int(input())
N = [int(input()) for _ in range(n)]

s = str(sum(N))
print(s[1:] + s[0])