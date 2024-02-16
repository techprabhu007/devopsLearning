import os

# Retrieve Ngrok auth token from environment variable
# token = os.getenv('NGROK_AUTH_TOKEN')

from flask import Flask

# from flask_ngrokpy import run_with_ngrok

app = Flask(__name__)
# run_with_ngrok(app)  # Start ngrok when app is run


@app.route("/")
def hello():
    return "Hello World!"


if __name__ == '__main__':
    app.run(host="0.0.0.0")
