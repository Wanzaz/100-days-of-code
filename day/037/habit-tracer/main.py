import os
import requests
from datetime import datetime

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

USERNAME = "wanzaz"
PIXELA_TOKEN = os.environ.get("PIXELA_WANZAZ_TOKEN")
GRAPH_ID = "graph1"


# 1. Creating my user account
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}

# response = requests.post(url=pixela_endpoint, json=user_params)
# response.raise_for_status()
# print(response.text)


# 2. Creating a grah definition
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": GRAPH_ID,
    "name": "Cycling Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai",
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN,
}


# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# https://pixe.la/v1/users/wanzaz/graphs/graph1.html
# print(response.text)


# 3. Posting value to the graph
pixel_creation_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"
today = datetime.today().strftime(f"%Y%m%d")

pixel_data = {
    "date": today,
    "quantity": "5.11",
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)
