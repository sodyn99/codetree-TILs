m1, d1, m2, d2 = map(int, input().split())

num_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']

t = 0
now_day = ''
if m2 > m1 or (m2 == m1 and d2 > d1):
    while not (m1 == m2 and d1 == d2):
        d1 += 1
        t += 1
        if d1 > num_of_days[m1-1]:
            d1 = 1
            m1 += 1
    now_day = days[t % 7]

elif m1 > m2 or (m1 == m2 and d1 > d2):
    while not (m1 == m2 and d1 == d2):
        d2 += 1
        t += 1
        if d2 > num_of_days[m2-1]:
            d2 = 1
            m2 += 1
    days = days[:1] + days[1:][::-1]
    now_day = days[t % 7]
    
else:
    now_day = days[0]

print(now_day)