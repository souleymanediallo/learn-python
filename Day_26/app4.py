weather_c = {
    "Monday": 12,
    "Tuesday": 24,
    "Wednesday": 23,
    "Thursday": 21,
    "Friday": 14,
    "Saturday": 10,
    "Sunday": 29,
}

new_weather = {k: (v * 9 / 5) + 32 for (k, v) in weather_c.items()}
print(new_weather)
