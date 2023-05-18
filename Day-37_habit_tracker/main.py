import requests
from datetime import datetime

USERNAME = "irinabubu"
TOKEN = "dd6w8jwa8daf7a"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=pixela_endpoint, json=user_params)
#print(response.text)

graphs_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graphs_config = {
    "id": GRAPH_ID,
    "name": "Walking Running Distance",
    "unit": "km",
    "type": "float",
    "color": "ajisai"
}

headers = {
    "X-USER-TOKEN": TOKEN
}

#response = requests.post(url=graphs_endpoint, json=graphs_config, headers=headers)
#print(response.text)

graph_value_endpoint = f"{graphs_endpoint}/{GRAPH_ID}"

today = datetime.now()
#print(today.strftime("%Y%m%d"))


graph_values = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many kilometer did you wolk today?:")
}

response = requests.post(url=graph_value_endpoint, json=graph_values, headers=headers)
print(response.text)

update_pixel_endpoint = f"{graph_value_endpoint}/{today.strftime('%Y%m%d')}"

update_values = {
    "quantity": "6.23"
}

#response = requests.put(url=update_pixel_endpoint, json=update_values, headers=headers)

delete_pixel_endpoint = f"{graph_value_endpoint}/{today.strftime('%Y%m%d')}"
#response = requests.delete(url=delete_pixel_endpoint, headers=headers)
#print(response.text)

