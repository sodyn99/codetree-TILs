N, K  = map(int, input().split())
people = [0 for _ in range(10000)]

for _ in range(N):
    p, a = input().split()
    p = int(p)
    if a == 'G':
        a = 1
    else:
        a = 2
    people[p-1] = a

m = 0
for i in range(len(people)-K+1):
    s = sum(people[i:i+K+1])
    m = max(m, s)

print(m)
