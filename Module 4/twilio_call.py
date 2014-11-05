#reference: https://www.twilio.com/docs/quickstart/python/sms/sending-via-rest
# Download the twilio-python library from http://twilio.com/docs/libraries

import twilio
from twilio.rest import TwilioRestClient

def inform_phone(message):

    account = "Your Twilio account number"

    token = "Token received from Twilio"


    client = TwilioRestClient(account, token)
    
    # code for sending a message
    call = client.messages.create(to="Receiver",  from_="Your Twilio number" , body=message)

    
    # Generate a message by going to twimlets.com and select Simple Message and use the resulting URL
    call = client.calls.create(url="Message URL",  to="Your Twilio number", from_="Receiver")

    print call.sid


def main():
    inform_phone("test")

if __name__=="__main__":
    main()
