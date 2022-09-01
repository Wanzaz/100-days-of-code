import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TEQUILA_API_KEY = os.environ.get("TEQUILA_KIWI_API_KEY")
TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"


class FlightSearch:

    def get_destination_code(self, city_name):
        location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
        headers = {"apikey": TEQUILA_API_KEY}
        query = {"term": city_name, "location_types": "city"}

        search_response = requests.get(
                url=location_endpoint,
                headers=headers,
                params=query
        )
        results = search_response.json()["locations"]
        code = results[0]["code"]
        return code




        


