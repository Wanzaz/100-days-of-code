# --- This code doesn't work it returns SSL error with expired certificates ---

import ssl
import time
import smtplib
import requests
from datetime import datetime

with open("../../../passwords.txt") as passwords_data:
    EMAIL_PASSWORD = passwords_data.readline()
EMAIL_SENDER = "wanzaz.contact@gmail.com"

MY_LAT = 51.507351 # Your latitude
MY_LONG = -0.127758 # Your longitude


def is_iss_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    #Your position is within +5 or -5 degrees of the ISS position.
    if MY_LAT-5 <= iss_latitude <= MY_LAT+5 and MY_LONG-5 <= iss_longitude <= MY_LONG+5:
        return True


def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }
    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    time_now = datetime.now().hour


    if time_now >= sunset or time_now <= sunrise:
        return True


while True:
    time.sleep(60)
    if is_iss_overhead() and is_night():
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
            connection.login(user=EMAIL_SENDER, password=EMAIL_PASSWORD)
            connection.sendmail(
                from_addr=EMAIL_SENDER,
                to_addrs=EMAIL_SENDER,
                msg=f"Subject:Look up!\n\n The ISS is above you in the sky.")

