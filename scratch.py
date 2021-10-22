import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

execution = client.studio \
                  .flows('FW6e34382992fb959be21296834c3f5525') \
                  .executions \
                  .create(to='+918870539376', from_='+18182966662')

print(execution.sid)
