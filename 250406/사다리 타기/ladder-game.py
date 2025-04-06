N, M = map(int, input().split())
ladder = [tuple(map(int, input().split())) for _ in range(M)]

def go_ladder(ladder):
    people = [i+1 for i in range(N)]
    ladder.sort(key = lambda x: x[1])
    tmp = 0
    for a, b in ladder:
        tmp = people[a-1]
        people[a-1] = people[a]
        people[a] = tmp

    return people

result_0 = go_ladder(ladder)

cnt = M
ladder_new = []
def dfs(n, c):
    global cnt
    if n == M:
        if go_ladder(ladder_new) == result_0:
            cnt = min(cnt, c)
        return
    
    # 선택 할 때
    ladder_new.append(ladder[n])
    dfs(n+1, c+1)
    ladder_new.pop()

    # 선택 안 할 때
    dfs(n+1, c)

dfs(0, 0)
print(cnt)