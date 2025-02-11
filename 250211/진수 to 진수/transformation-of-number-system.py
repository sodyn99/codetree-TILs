a, b = map(int, input().split())
n = input()

# Write your code here!

def to_decimal(n, k):
    s = 0
    for i in n:
        s = s * k + int(i)
    return s

def to_k(n, k):
    arr = []
    while True:
        if n < k:
            arr.append(n)
            break
        arr.append(n % k)
        n //= k
    return "".join(map(str, arr[::-1]))

print(to_k(to_decimal(n, a), b))