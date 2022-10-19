# server.py

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=["GET"])
def server_status():
    return "Server is on."


@app.route("/info", methods=["GET"])
def information():
    x = "This website will calculated blood cholesterol levels.\n"
    x += "It is written by David Ward."
    return x


if __name__ == "__main__":
    app.run()
