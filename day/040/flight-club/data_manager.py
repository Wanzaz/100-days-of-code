import os
import requests
from pprint import pprint
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

SHEET_BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")
SHEETY_PRICES_ENDPOINT = "https://api.sheety.co/50c8f5d9fdd2c424bd1fde484c730d64/flightPrices/prices"
HEADERS = {
    "Authorization": f"Bearer {SHEET_BEARER_TOKEN}"
}


class DataManager:

    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHEETY_PRICES_ENDPOINT, headers=HEADERS)
        data = response.json()
        self.destination_data = data["prices"]
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(
                url=f"{SHEETY_PRICES_ENDPOINT}/{city['id']}",
                json=new_data,
                headers=HEADERS
            )
            pprint(response.text)

