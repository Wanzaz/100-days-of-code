# ---Stock Trading News Alert App---

import os
import ssl
import smtplib
import requests
from datetime import datetime

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
PRICE_API_KEY = os.environ.get("AV_STOCK_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_WANZAZ_API_KEY")
EMAIL_PASSWORD = os.environ.get("EMAIL_WANZAZ_PASSWORD")
EMAIL_SENDER = "wanzaz.contact@gmail.com"
EMAIL_RECEIVER = "wanzaz.contact@gmail.com"

price_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": PRICE_API_KEY,
}

response = requests.get(url=AV_ENDPOINT, params=price_parameters)
stock_data = response.json()

before_yesterday = datetime.now().day - 4
before_yesterday_date = datetime.today().strftime(f"%Y-%m-{before_yesterday}")
yesterday = datetime.now().day - 3
yesterday_date = datetime.today().strftime(f"%Y-%m-{yesterday}")

# Prices closed before yesterday and yesterday
price_b4_yda = float(stock_data["Time Series (Daily)"][before_yesterday_date]["4. close"])
price_yda = float(stock_data["Time Series (Daily)"][yesterday_date]["4. close"])
print(f"TSLA price before yesterday: {price_b4_yda}$\nTSLA price yesterday: {price_yda}$")

# Differences between closed prices
decrease = (price_b4_yda - price_yda) / price_b4_yda * 100
increase = (price_yda - price_b4_yda) / price_yda * 100
difference, status = (round(increase, 1), "up") if increase > decrease else (round(decrease, 1), "down")

if difference > 2:
    news_parameters = {
        "q": COMPANY_NAME,
        "apiKey": NEWS_API_KEY,
    }
    response = requests.get(url=NEWS_ENDPOINT, params=news_parameters)
    news_data = response.json()["articles"][0]

    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as connection:
        connection.login(user=EMAIL_SENDER, password=EMAIL_PASSWORD)
        connection.sendmail(
            from_addr=EMAIL_SENDER,
            to_addrs=EMAIL_RECEIVER,
            msg=f"Subject:Tesla Stock News\n\n{STOCK}: {difference} % {status}\nHeadline: {news_data['title']} \nBrief: {news_data['description']}\nLink: {news_data['url']}")


