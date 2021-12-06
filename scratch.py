import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = "ACd25b0b811ff8f87820ca9fbe03f75ded"
auth_token = "9b3f1cc7aad65389f3b286b6aceb2c3e"
client = Client(account_sid, auth_token)

call = client.calls \
    .create(
    machine_detection='Enable',
    url='https://handler.twilio.com/twiml/EH8ccdbd7f0b8fe34357da8ce87ebe5a16',
    to='+918870539376',
    from_='+17377778443'
)

print(call.sid)
