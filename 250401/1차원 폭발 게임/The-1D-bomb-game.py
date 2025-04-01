N, M = map(int, input().split())
bombs = [int(input()) for _ in range(N)]

n = 0
while True:
    t = 1
    tmp_arr = []
    for i in range(1, len(bombs)):
        if bombs[i] == bombs[i-1]:
            t += 1
            if t >= M:
                if i + 1 < len(bombs):
                    if bombs[i+1] != bombs[i]:
                        for j in range(i-t+1, i+1):
                            bombs[j] = 0
                        t = 1
                elif i == len(bombs) - 1:
                    for j in range(i-t+1, i+1):
                        bombs[j] = 0
                    t = 1
    for b in bombs:
        if b != 0:
            tmp_arr.append(b)
    bombs = tmp_arr
    n += 1
    if n > N:
        break

print(len(bombs))
for b in bombs:
    print(b)