import random


def get_weather_data():
    return random.randrange(90, 110)


print([temp for _ in range(20) if (temp := get_weather_data()) >= 100])
