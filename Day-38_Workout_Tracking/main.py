import requests
from datetime import datetime

APP_ID = "234a9adb"
APP_KEY = "2568f833db7cc9d92911f7251f4645b4"
TOKEN = "aasdad7sdfn3e2"

exercises_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"
header = {
     'x-app-id': APP_ID,
     'x-app-key': APP_KEY,
     'x-user-jwt': TOKEN

}
exercise_text = input("Tell me which exercises you did: ")

body = {
 "query": exercise_text,
 "gender": "female",
 "weight_kg": 58.8,
 "height_cm": 169,
 "age": 30
}

response = requests.post(url=exercises_endpoint, json=body, headers=header)
response.raise_for_status()
#print(response.text)

data = response.json()["exercises"]
#exercises = [item["user_input"] for item in data]
#duration = [item["duration_min"] for item in data]
#calories = [item["nf_calories"] for item in data]

header_sheety = {"Authorization": "Bearer ssdff454rffe4rdmgnmfk5"}

add_data_endpoint = "https://api.sheety.co/66ae66f1c68d2e2c02709b5c44ab2bae/workoutTracking/workouts"
today = datetime.now().strftime('%d/%m/%Y')
time = datetime.now().strftime("%X")
for exercise in data:
    workout_data = {
     "workout": {
        "date": today,
        "time": time,
        "exercise": exercise["name"].title(),
        "duration": exercise["duration_min"],
        "calories": exercise["nf_calories"]
      }
    }

    response_new = requests.post(url=exercises_endpoint, json=workout_data, headers=header_sheety)
    print(response_new.text)
