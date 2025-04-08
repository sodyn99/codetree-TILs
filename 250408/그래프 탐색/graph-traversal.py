N, M = map(int, input().split())
graph = [[] for _ in range(N+1)]

for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

visited = [False for _ in range(N+1)]
visited[1] = True

cnt = 0
def dfs(n):
    global cnt
    
    for i in graph[n]:
        if not visited[i]:
            visited[i] = True
            cnt += 1
            dfs(i)

dfs(1)
print(cnt)

    