N, C, G, H = map(int, input().split())
Temp = [tuple(map(int, input().split())) for _ in range(N)]

def work_by_machine(t, Ta, Tb):
    work = 0
    if t < Ta:
        work = C
    elif t <= Tb:
        work = G
    else:
        work = H
    return work
    

max_work = 0
for t in range(1000):
    max_work_by_machine = 0
    for T in Temp:
        max_work_by_machine += work_by_machine(t, T[0], T[1])
    max_work = max(max_work, max_work_by_machine)

print(max_work)