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

result_date = "2100-00-00"
result_day = ""
result_weather = ""
for rain in rains:
    if rain.weather == "Rain":
        if rain.date < result_date:
            result_date = rain.date
            result_day = rain.day
            result_weather = rain.weather

print(result_date, result_day, result_weather)
