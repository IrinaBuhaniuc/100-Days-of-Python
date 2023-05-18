import requests
from twilio.rest import Client

account_sid = "AC4762d59057a74d920caa8edd0ffbfc73"
auth_token = "f28b40a604dbc0231ddc4dfe53ea3d2e"

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
API_KEY_PRICE = "J4S1MKATIBD1OYI1"

API_KEY_NEWS = "ebc11a8a4ffa4b9ebd82378f7c22581f"

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": API_KEY_PRICE

}

parameters_news = {
                "apiKey": API_KEY_NEWS,
                "q": COMPANY_NAME,
                "category": "business",
                "language": 'en',
}

response = requests.get("https://www.alphavantage.co/query", parameters)
response.raise_for_status()
data_price = response.json()["Time Series (Daily)"]

date_list = []
close_price_list = []
for data in data_price:
    date_list.append(data)

for date in date_list:
    close_price = data_price[date]["4. close"]
    close_price_list.append(close_price)

price_difference = abs(float(close_price_list[0]) - float(close_price_list[1]))
percentage_difference = round(price_difference*100/float(close_price_list[1]), 2)
print(close_price_list[0], close_price_list[1])
print(percentage_difference)


top_headlines = requests.get("https://newsapi.org/v2/top-headlines", parameters_news)
data_news = top_headlines.json()["articles"]
last_news_title = []
last_news_description = []
articles = data_news[:3]
print(articles)
for n in range(0, len(articles)):
    last_news_title.append(articles[n]["title"])
    last_news_description.append(articles[n]["description"])
print(last_news_title)
print(last_news_description[0])

messages_to_send = [f"Headline: {item['title']}. \nBrief: {item['description']}" for item in articles]
print(messages_to_send)

for message in messages_to_send:

    if close_price_list[0] > close_price_list[1]:
        client = Client(account_sid, auth_token)
        message = client.messages \
                .create(
                body=f"TSLA: 🔺{percentage_difference}% \n{message}",
                from_="+19807377369",
                to="+49 173 9314100",
        )

    else:
        percentage_difference = percentage_difference * (-1)
        client = Client(account_sid, auth_token)
        message = client.messages \
            .create(
            body=f"TSLA: 🔻{percentage_difference}%  \n{message}",
            from_="+19807377369",
            to="+49 173 9314100",
        )


