m1, d1, m2, d2 = map(int, input().split())

# Write your code here!

day_of_week = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def num_of_days(m, d):
    days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(0, m-1):
        total += days[i]
    total += d
    return total

d = num_of_days(m2, d2) - num_of_days(m1, d1)
while d < 0:
    d += 7

print(day_of_week[d%7])