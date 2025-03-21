N = int(input())
blocks = [int(input()) for _ in range(N)]
removes = [tuple(map(int, input().split())) for _ in range(2)]

t1 = []
t2 = []
for i in range(N):
    if i in range(removes[0][0]-1, removes[0][1]):
        continue
    else:
        t1.append(blocks[i])

for i in range(len(t1)):
    if i in range(removes[1][0]-1, removes[1][1]):
        continue
    else:
        t2.append(t1[i])

print(len(t2))
for t in t2:
    print(t)