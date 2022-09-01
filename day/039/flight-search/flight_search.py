import os
import requests
from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

TEQUILA_API_KEY = os.environ.get("TEQUILA_KIWI_API_KEY")


class FlightSearch:

    def get_destination_code(self, city_name):
        # Return "TESTING" for now to make sure Sheety is working. Get TEQUILA API data later.
        code = "TESTING"
        return code




        


