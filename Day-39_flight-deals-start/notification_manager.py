from twilio.rest import Client

TWILIO_SID = "AC4762d59057a74d920caa8edd0ffbfc73"
TWILIO_AUTH_TOKEN = "f28b40a604dbc0231ddc4dfe53ea3d2e"
TWILIO_VIRTUAL_NUMBER = "+19807377369"
TWILIO_VERIFIED_NUMBER = "+49 173 9314100"


class NotificationManager:

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
