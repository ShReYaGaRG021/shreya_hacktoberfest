# Maciej Sikora
# Github id: maciek04786
#
# This is a rain alert app, which tells you whether it will rain today,
# based on coordinates given in weather_parameters, it uses open weather
# map api, registration is free

import requests

weather_parameters = {
    "lat": 50.394050,
    "lon": -3.516020,
    "appid": "Your open weather map api id",
    "exclude": "current,minutely,daily,alerts"
}

response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
hourly_data = weather_data["hourly"][:12]

will_rain = False

for hour in hourly_data:
    if hour["weather"][0]["id"] < 700:
        will_rain = True
        break

if will_rain:
    print("It will rain today! Don't forget your umbrella ☂")
else:
    print("There's no rain in the forecast for today! 😊")
