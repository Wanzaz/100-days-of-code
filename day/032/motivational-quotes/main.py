import ssl
import smtplib
import datetime as dt
from random import choice

# Email Information
EMAIL_SENDER = "wanzaz.contact@gmail.com"
EMAIL_RECEIVER = "wanzaz.contact@yahoo.com"
with open("../../../passwords.txt") as passwords_file:
    EMAIL_PASSWORD = passwords_file.readline()


# Datetime
now = dt.datetime.now()
weekday = now.weekday()

if weekday == 3:
    # Motivational Quote content
    subject = "Monday Motivation"
    with open("quotes.txt") as quotes_file:
        all_quotes = quotes_file.readlines()
        quote = choice(all_quotes)

    context = ssl.create_default_context()

    # Creating new Email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(user=EMAIL_SENDER, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_SENDER,
            to_addrs=EMAIL_RECEIVER,
            msg=f"Subject:{subject}\n\nQuote: {quote} ")
else:
    print("Today isn't Monday!")

