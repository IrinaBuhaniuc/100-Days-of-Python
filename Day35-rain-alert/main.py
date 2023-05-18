import requests
from twilio.rest import Client

API_KEY = "4e8524426d4cc197491fe4065621284c"
LAT = 52.1521636
LNG = 9.9513046

account_sid = "AC4762d59057a74d920caa8edd0ffbfc73"
auth_token = "f28b40a604dbc0231ddc4dfe53ea3d2e"

parameters = {
    "lat": LAT,
    "lon": LNG,
    "appid": API_KEY,
    "exclude": "current,minutely,daily"

}

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=parameters)
response.raise_for_status()
weather_data = response.json()

#weather_list = []
#weather_id_list = []

#for n in range(0, 12):
#    weather_list.append(weather_data[n]["weather"])
#    weather_id_list.append(weather_list[n][0]["id"])

#    if weather_id_list[n] <= 800:
 #       print("Today it's gonna rain")
will_rain = False
weather_slice = weather_data["hourly"][:12]

for hour_data in weather_slice:
    if hour_data["weather"][0]["id"] < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="It's going to rain today. Remember to bring an ☔️☔️.",
        from_="+19807377369",
        to="+49 173 9314100",
    )
else:
    client = Client(account_sid, auth_token)
    message = client.messages \
        .create(
        body="Today you don't need a ☔️☔️",
        from_="+19807377369",
        to="+49 173 9314100",
    )







