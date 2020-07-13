from twilio.rest import Client
from os import environ

def sendMessage(body):
    account_sid = environ.get('twillio_sid')
    auth_token = environ.get('twillio_token')
    client = Client(account_sid, auth_token)
    message = client.messages.create(body=body,from_='whatsapp:+14155238886',to='whatsapp:+5512996272121')
    return message.status
