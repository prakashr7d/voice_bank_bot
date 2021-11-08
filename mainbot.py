import requests
from flask import Flask
from flask import request, jsonify

from google_voice import GoogleRecognise

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
                             jsshson={"sender": sender, "message": text})
    return jsonify(response.json())


# main driver function
if __name__ == '__main__':
    # run() method of Flask class runs the application
    # on the local development server.
    app.run(port=2001, host="0.0.0.0")
