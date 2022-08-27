# ---Using API Keys to Authenticate and Get the Weather from OpenWeatherMap---

import json
import requests

OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
with open("../../../api_key.txt") as key:
    API_KEY = key.read()[:32]
MY_LON = -118.24
MY_LAT = 34.052

# https://api.openweathermap.org/data/2.5/weather?q={city name},{country code}&appid={API key}
# https://api.openweathermap.org/data/3.0/onecall?lat={lat}&lon={lon}&exclude={part}&appid={API key}
weather_parameters = {
    "lat": MY_LAT,
    "lon": MY_LON,
    "appid": API_KEY,
    "exclude": "current,minutely,daily",
}

response = requests.get(url=OWN_Endpoint, params=weather_parameters)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["hourly"][:12]

will_rain = False

for hour_data in weather_slice:
    condition_code = hour_data["weather"][0]["id"]
    if int(condition_code) < 700:
        will_rain = True

if will_rain:
    print("Bring an Umbrella.")



# PREVIOUS CODE
# hour_condition = []
# for hour in range(12):
#     weather_data_id = response.json()["hourly"][hour]["weather"][0]["id"]
#     hour_condition.append(weather_data_id)

# for condition in hour_condition:
#     if condition < 700:
#         print("Bring an Umbrella!")
#         break

# print(hour_condition)


