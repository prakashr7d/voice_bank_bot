import contextlib
import pathlib
import time
import wave

from flask import Flask, request
from gtts import gTTS
from playsound import playsound

from constants import duration

app = Flask(__name__)


@app.route("/speak", methods=['GET'])
def speech() -> str:
    if request.method == 'GET':
        message = request.json.get('message')
        print(message)
        playsound(f'{message}', False)

        time.sleep(duration.get(message))
        return "success"


app.run(port=3011)
