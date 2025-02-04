m1, d1, m2, d2 = map(int, input().split())
A = input()

# Write your code here!

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

def num_of_days(m, d):
    day_of_week = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    total = 0
    for i in range(m-1):
        total += day_of_week[i]
    total += d
    return total

diff = num_of_days(m2, d2) - num_of_days(m1, d1)
result = diff // 7
for i in range(len(days)):
    if A == days[i] and i > diff % 7:
        result += 1
print(result)