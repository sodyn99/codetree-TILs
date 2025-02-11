N = input()

# Write your code here!

def to_binary(n):
    arr = []
    while True:
        if n < 2:
            arr.append(n)
            break
        arr.append(n % 2)
        n //= 2
    return "".join(map(str, arr[::-1]))

def to_decimal(n):
    s = 0
    for i in n:
        s = s * 2 + int(i)
    return s

print(to_binary(to_decimal(N) * 17))