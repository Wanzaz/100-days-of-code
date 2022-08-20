# --- This code doesn't work it returns SSL error with expired certificates ---

import requests
from datetime import datatime


MY_LAT = 51.507351
MY_LOG = -0.127758


parameters = {
    "lat": MY_LAT,
    "lng": MY_LOG,
    "formatted": 0,
} # only two required parameters

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data ["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datatime.now()

print(time_now.hour)
