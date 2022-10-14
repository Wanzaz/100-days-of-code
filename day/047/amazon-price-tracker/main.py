# import lxml
import os 
import ssl
import smtplib
import requests
from bs4 import BeautifulSoup

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

EMAIL_PASSWORD = os.environ.get("EMAIL_WANZAZ_PASSWORD")
EMAIL_SENDER = "wanzaz.contact@gmail.com"
EMAIL_RECEIVER = "wanzaz.contact@gmail.com"
message = f""


USER_AGENT = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/104.0.5112.81 Safari/537.36"
ACCEPT_LANGUAGE = "en-GB;q=0.8"
PRODUCT_URL = "https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"



def send_alert_email(product_price, product_title):
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", port=465, context=context) as connection:
        connection.login(user=EMAIL_SENDER, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_SENDER,
            to_addrs=EMAIL_RECEIVER,
            msg=f"Subject:Amazon Price Alert!\n\n{product_title} is now {product_price}\n{PRODUCT_URL}"
        )


# Request to product website
headers = {"Accept-Language" : ACCEPT_LANGUAGE,
           "User-Agent": USER_AGENT}


response = requests.get(url=PRODUCT_URL, headers=headers)


# Webscraping product website
product_webpage = response.text
soup = BeautifulSoup(product_webpage, "html.parser") # could be lxml parser also
product = soup.find(name="span", class_="a-price a-text-price a-size-medium apexPriceToPay").find_next(name="span", class_="a-offscreen")
product_title = soup.find(name="span", id="productTitle").getText().strip().replace("\xe9", "e")
product_price = float(product.getText().split("$")[1])

if product_price < 350:
    send_alert_email(product_price, product_title)

