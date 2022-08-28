# ---Stock Trading News Alert App---

import os
import ssl
import smtplib
import requests
from datetime import datetime


STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
AV_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
PRICE_API_KEY = os.environ.get("ALPHA_VANTAGE_API_KEY")
NEWS_API_KEY = os.environ.get("NEWS_API_KEY")
EMAIL_PASSWORD = os.environ.get("EMAIL_PASSWORD")
EMAIL_SENDER = "wanzaz.contact@gmail.com"
EMAIL_RECEIVER = "wanzaz.contact@gmail.com"

price_parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": PRICE_API_KEY,
}

response = requests.get(url=AV_ENDPOINT, params=price_parameters)
stock_data = response.json()

before_yesterday = datetime.now().day - 3
before_yesterday_date = datetime.today().strftime(f"%Y-%m-{before_yesterday}")
yesterday = datetime.now().day - 2
yesterday_date = datetime.today().strftime(f"%Y-%m-{yesterday}")

# Highest and Lowest prices of before yesterday and yesterday
# low_price_b4_yda = float(stock_data["Time Series (Daily)"][before_yesterday_date]["3. low"])
# high_price_b4_yda = float(stock_data["Time Series (Daily)"][before_yesterday_date]["2. high"])
# low_price_yda = float(stock_data["Time Series (Daily)"][yesterday_date]["3. low"])
# high_price_yda = float(stock_data["Time Series (Daily)"][yesterday_date]["2. high"])
# print(f"Lowest prices: \n  before yesterday: {low_price_b4_yda} \n  yesterday: {low_price_yda} \nHighest Prices: \n  before yesterday: {high_price_b4_yda}\n  yesterday: {high_price_yda}")

# Prices closed before yesterday and yesterday
price_b4_yda = float(stock_data["Time Series (Daily)"][before_yesterday_date]["4. close"])
price_yda = float(stock_data["Time Series (Daily)"][yesterday_date]["4. close"])
print(f"TSLA price before yesterday: {price_b4_yda}$\nTSLA price yesterday: {price_yda}$")

# Differences between highs and lows during the two days
# decrease = (high_price_b4_yda - low_price_yda) / high_price_b4_yda * 100
# increase = (high_price_yda - low_price_b4_yda) / high_price_yda * 100
# biggest_diff, emoji = (increase, "🔺") if increase > decrease else (decrease, "🔻")

# Differences between closed prices
decrease = (price_b4_yda - price_yda) / price_b4_yda * 100
increase = (price_yda - price_b4_yda) / price_yda * 100
difference, status = (round(increase, 1), "up") if increase > decrease else (round(decrease, 1), "down")

if difference > 5:
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
            msg=f"Subject:Tesla Stock News\n\nTSLA: {difference} % {status}\nHeadline: {news_data['title']} \nBrief: {news_data['description']}\nLink: {news_data['url']}")

