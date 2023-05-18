import requests
from datetime import datetime


header_sheety = {"Authorization": "Bearer ssdff454rffe4rdmgnmfk5"}


endpoint = "https://api.sheety.co/66ae66f1c68d2e2c02709b5c44ab2bae/test/tabellenblatt1"
today = datetime.now()
time = today.time()
data = {
    "tabellenblatt1": {
        "date": today.strftime('%d/%m/%Y'),
        "time": time.strftime('%X'),
        "exercise": "run",
        "duration": "4:56",
        "calories": "154",
        }
    }

response = requests.post(url=endpoint, json=data, headers=header_sheety)
response.raise_for_status()
print(response.text)