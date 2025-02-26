n, m = map(int, input().split())

# Process robot A's movements
t = []
d = []
for _ in range(n):
    time, direction = input().split()
    t.append(int(time))
    d.append(direction)

# Process robot B's movements
t_b = []
d_b = []
for _ in range(m):
    time, direction = input().split()
    t_b.append(int(time))
    d_b.append(direction)

# Please write your code here.

p_a, p_b = [], []
a, b = 0, 0
for i in range(n):
    for j in range(t[i]):
        if d[i] == 'L':
            a -= 1
        else:
            a += 1
        p_a.append(a)
for i in range(m):
    for j in range(t_b[i]):
        if d_b[i] == 'L':
            b -= 1
        else:
            b += 1
        p_b.append(b)

if len(p_a) > len(p_b):
    for _ in range(len(p_a) - len(p_b)):
        p_b.append(p_b[-1])
elif len(p_a) < len(p_b):
    for _ in range(len(p_b) - len(p_a)):
        p_a.append(p_a[-1])

meet_num = 0
for i in range(len(p_a)):
    if i == 0 or p_a[i-1] != p_b[i-1]:
        if p_a[i] == p_b[i]:
            meet_num += 1

print(meet_num)