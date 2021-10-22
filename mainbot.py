import requests
from playsound import playsound
while True:
    text = input("Enter Your message:")
    requests.post(url="http://localhost:2001/webhooks/callback/webhook", json={"sender": "me", "message": text})

