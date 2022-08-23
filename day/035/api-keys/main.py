# ---Using API Keys to Authenticate and Get the Weather from OpenWeatherMap---

import requests

OWN_Endpoint = "https://api.openweathermap.org/data/2.5/weather"
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
}

response = requests.get(url=OWN_Endpoint, params=weather_parameters)
response.raise_for_status()
data = response.json()
print(data)

