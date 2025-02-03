n = int(input())
date = []
day = []
weather = []

for _ in range(n):
    d, dy, w = input().split()
    date.append(d)
    day.append(dy)
    weather.append(w)

# Write your code here!

class Rain:
    def __init__(self, date, day, weather):
        self.date = date
        self.day = day
        self.weather = weather

rains = [Rain(date[i], day[i], weather[i]) for i in range(n)]

result = ("2100-00-00", "", "")
for rain in rains:
    if rain.weather == "Rain":
        if rain.date < result[0]:
            result = rain.date, rain.day, rain.weather

print(*result)
