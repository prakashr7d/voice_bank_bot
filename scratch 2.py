from flask import Flask, request

app = Flask(__name__)


@app.route("/message", methods=["GET", "POST"])
def message():
    print(request.json)
    print(request.data)
    return "success"

app.run(port=2004, debug=True)