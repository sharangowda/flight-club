from twilio.rest import Client
from sheets import *

# You can use SMTP module as well if you want it to be sent to your email.


class NotificationManager:
    def __init__(self):
        # Use your twilio account SID.
        self.twilio_account_sid = 'TWILIO_ACC_SID'
        # Use your twilio account token.
        self.twilio_auth_token = 'TWILIO_AUTH_TOKEN'
        # Use twilio account phone number.
        self.twilio_phone_number = +1234567890
        data = Auth()
        self.body = data.make_dict()

    def send_data(self):
        client = Client(self.twilio_account_sid,
                        self.twilio_auth_token)
        message = client.messages.create(
            body=f"Today's flight charges:\n\n{self.body}", from_=self.twilio_phone_number, to=+1234567890)  # Enter your phone number to get the messages.
