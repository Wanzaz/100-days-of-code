import os
import requests
from pprint import pprint
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())


from data_manager import DataManager
from flight_search import FlightSearch

data_manager = DataManager()
sheet_data = data_manager.get_destination_data()


if sheet_data[0]["iataCode"] == "":
    flight_search = FlightSearch()
    for row in sheet_data:
        row["iataCode"] = flight_search.get_destination_code(row["city"])
    pprint(sheet_data)

    data_manager.destination_data = sheet_data
    data_manager.update_destination_codes()

