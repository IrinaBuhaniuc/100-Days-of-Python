import requests
from datetime import datetime

MY_LAT = 52.154778
MY_LNG = 9.9579652
#response = requests.get(url="http://api.open-notify.org/iss-now.json")
#response.raise_for_status()

#data = response.json()
#longitude = data["iss_position"]["longitude"]
#latitude = data["iss_position"]["latitude"]
#iss_position = (longitude, latitude)
#print(iss_position)

parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted":0
}

response = requests.get("https://api.sunrise-sunset.org/json", parameters)
response.raise_for_status()

data = response.json()
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]
print(sunrise, sunset)


time_now = datetime.now()
time_hour = time_now.hour
print(time_now)

if time_hour > int(sunrise):
    print("Hallo")