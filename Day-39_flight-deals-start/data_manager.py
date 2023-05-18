import requests
from pprint import pprint

SHETTY_ENDPOINT = "https://api.sheety.co/66ae66f1c68d2e2c02709b5c44ab2bae/myFlightDeals/prices"

class DataManager:
    def __init__(self):
        self.destination_data = {}

    def get_destination_data(self):
        response = requests.get(url=SHETTY_ENDPOINT)
        self.destination_data = response.json()["prices"]
        #pprint(self.destination_data)
        return self.destination_data

    def update_destination_codes(self):
        for city in self.destination_data:
            new_data = {
                "price": {
                    "iataCode": city["iataCode"]
                }
            }
            response = requests.put(url=f"{SHETTY_ENDPOINT}/{city['id']}", json=new_data)
            print(response.text)