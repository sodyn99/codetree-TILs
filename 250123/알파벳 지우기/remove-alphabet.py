s = [input() for _ in range(2)]
s1, s2 = s

def num(s):
    S = ""
    for i in s:
        if i.isdigit():
            S += i
        else:
            continue
    return int(S)

print(num(s1) + num(s2))