import os

from flask import Flask


app = Flask(__name__)


@app.route("/")
def hello():
    username = os.getenv('SECRET_USERNAME')
    userpassword = os.getenv('SECRET_PASSWORD')
    return f"Hello from Python! v5 {username=} -- {userpassword=}"


@app.route("/health")
def health():
    return "ok"


if __name__ == "__main__":
    app.run(host='0.0.0.0')
