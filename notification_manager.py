from twilio.rest import Client

TWILIO_SID = "ACa0f8c8d22e69b4a3749b5adb1b820059"
TWILIO_AUTH_TOKEN = "7ae7e935c0f3cff93c0e78ac0b1bc32e"
TWILIO_VIRTUAL_NUMBER = "+17855041614"
TWILIO_VERIFIED_NUMBER = "+18436214388"


class NotificationManager:
    """
    This class is responsible for sending notifications with the deal flight details.
    """

    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        """
        Takes a message
        """
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_VIRTUAL_NUMBER,
            to=TWILIO_VERIFIED_NUMBER,
        )
        # Prints if successfully sent.
        print(message.sid)
