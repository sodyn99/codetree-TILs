N, M, K = map(int, input().split())
student = [int(input()) for _ in range(M)]

# Please write your code here.

arr = [0 for _ in range(N)]
pay = False
for i in range(M):
    for j in range(N):
        arr[student[i]-1] += 1
        if arr[j] >= K:
            pay = True
            print(j + 1)
            break
    if pay == True:
        break

if pay == False:
    print(-1)
