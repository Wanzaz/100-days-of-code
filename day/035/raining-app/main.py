# ---Using API Keys to Authenticate and Get the Weather from OpenWeatherMap---

import os
import ssl
import json
import smtplib
import requests

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


OWN_Endpoint = "https://api.openweathermap.org/data/3.0/onecall"
API_KEY = os.environ.get("OW_API_KEY")
MY_LON = -118.24
MY_LAT = 34.052
EMAIL_PASSWORD = os.environ.get("EMAIL_WANZAZ_PASSWORD")
EMAIL_SENDER = "wanzaz.contact@gmail.com"
EMAIL_RECEIVER = "wanzaz.contact@gmail.com"

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
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(user=EMAIL_SENDER, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_SENDER,
            to_addrs=EMAIL_RECEIVER,
            msg=f"Subject:Weather Warning\n\n Bring an Umbrella.")

