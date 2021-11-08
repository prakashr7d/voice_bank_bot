import requests
from playsound import playsound

from constants import DEFAULT_FILE_NAME
from google_voice import GoogleRecognise
from utils import record_audio
from flask import Flask
from flask import request, jsonify

app = Flask(__name__)


@app.route('/rasa', methods=['POST'])
def run_rasa():
    uri = request.json['g_uri']
    sender = request.json['sender_id']
    recognise = GoogleRecognise(uri)
    recognise.recognise()
    text = recognise.get_response()
    print(text)
    response = requests.post(url="http://localhost:5005/webhooks/rest/webhook",
                             json={"sender": sender, "message": text})
    return jsonify(response.json())


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run()
