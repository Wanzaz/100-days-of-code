import ssl
import random
import smtplib
import pandas as pd
import datetime as dt

# Constants
with open("../../../passwords.txt") as passwords_data:
    EMAIL_PASSWORD = passwords_data.readline()
EMAIL_SENDER = "wanzaz.contact@gmail.com"
NAME = "Wanzaz"
PLACEHOLDER = "[NAME]"
SUBJECT = "Your Birthday!"

# Datetime 
now = dt.datetime.now()
day = now.day
month = now.month


# Check if today matches a birthday in the birthdays.csv - DONE
people_info = pd.read_csv("birthdays.csv", index_col=0).to_dict()
if people_info["day"]["Wanzaz"] == day and people_info["month"]["Wanzaz"] == month:
    # If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name from birthdays.csv
    rand_num = random.randint(1, 3)
    with open(f"./letter-templates/letter_{rand_num}.txt") as letter_file:
        letter_contents = letter_file.read()
        email_body = letter_contents.replace(PLACEHOLDER, NAME)
        print(email_body)

    # Send the letter generated letter to that person's email address.
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(user=EMAIL_SENDER, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_SENDER,
            to_addrs=people_info["email"]["Wanzaz"],
            msg=f"Subject:{SUBJECT}\n\n {email_body}")




