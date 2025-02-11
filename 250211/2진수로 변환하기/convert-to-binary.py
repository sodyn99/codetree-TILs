n = int(input())

# Write your code here!
arr = []
while True:
    if n < 2:
        arr.append(n)
        break
    arr.append(n%2)
    n = n // 2

for a in arr[::-1]:
    print(a, end="")