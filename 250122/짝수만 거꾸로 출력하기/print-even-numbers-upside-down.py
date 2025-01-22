n = int(input())
arr = input().split()

for i in arr[::-1]:
    if int(i) % 2 == 0:
        print(i, end=" ")