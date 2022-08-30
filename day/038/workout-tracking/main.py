# ---Workout Tracking Using Google Sheets---

import os
import requests
from datetime import datetime

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

APP_ID = os.environ.get("NUTRITIONIX_APP_ID")
API_KEY = os.environ.get("NUTRITIONIX_API_KEY")
BEARER_TOKEN = os.environ.get("SHEETY_BEARER_TOKEN")

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
excercise_text = input("Tell me which excercises you did: ")

parameters = {
    "query": excercise_text,
    "gender": "male",
    "weight_kg": 96,
    "height_cm": 200.1,
    "age": 30
}

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}



response = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
# data = response.json()["exercises"][0]
result = response.json()

sheet_endpoint = "https://api.sheety.co/50c8f5d9fdd2c424bd1fde484c730d64/workoutTracking/list1"
headers = {
    "Authorization": f"Bearer {BEARER_TOKEN}"
}
today_date = datetime.now().strftime("%Y/%m/%d")
now_time = datetime.now().strftime("%H:%M:%S")

# My old version which was only for one activity at one time
# workout = {
#     "list1": {
#         "date": today_date,
#         "time": now_time,
#         "exercise": data["name"].title(),
#         "duration": data["duration_min"],
#         "calories": data["nf_calories"]
#     }
# }

# sheety_response = requests.post(url=sheet_endpoint, json=workout)
# print(sheety_response.text)

for exercise in result["exercises"]:
    sheet_inputs = {
        "list1": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheet_endpoint,
        json=sheet_inputs,
        headers=headers
    )

    # Second option of authentication
    # auth=(
    #   YOUR USERNAME, 
    #   YOUR PASSWORD,
    # )

    print(sheet_response.text)
