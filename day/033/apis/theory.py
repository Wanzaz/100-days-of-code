# API Endpoint = api.coinbase.com
# API Response Codes:
    # 1XX = Hold On - Informational
    # 2XX = Here You Go - Success
    # 3XX = Go Away - Redirection
    # 4XX = You Screwed Up - Client Error
    # 5XX = I Screwed Up - Server Error

import requests

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

# data = response.json()["iss_position"]
data = response.json()

longitude = data["iss_position"]["longitude"]
latitude = data["iss_position"]["latitude"]

iss_position = (longitude, latitude)
print(iss_position)
# https://www.latlong.net/Show-Latitude-Longitude.html - to figure out where the iss is
