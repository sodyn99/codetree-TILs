m1, d1, m2, d2 = map(int, input().split())

# Please write your code here.

num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

d = 0

while not (m1 == m2 and d1 == d2):
    d1 += 1
    d += 1
    if d1 > num_of_days[m1-1]:
        d1 = 0
        m1 += 1

print(d)