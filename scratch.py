import os
from twilio.rest import Client

# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = ""
auth_token = ""
client = Client(account_sid, auth_token)

call = client.calls \
    .create(
    machine_detection='Enable',
    url='https://handler.twilio.com/twiml/EH8ccdbd7f0b8fe34357da8ce87ebe5a16',
    to='+918870539376',
    from_='+17377778443'
)

print(call.sid)
