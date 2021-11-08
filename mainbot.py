import requests
from playsound import playsound

from constants import DEFAULT_FILE_NAME
from google_voice import GoogleRecognise
from utils import record_audio

while True:
    record_audio(DEFAULT_FILE_NAME)
    recognise = GoogleRecognise(DEFAULT_FILE_NAME)
    recognise.recognise()
    text = recognise.response()
    response = requests.post(url="http://localhost:2001/webhooks/callback/webhook",
                             json={"sender": "me", "message": text})
    print(response.json())



