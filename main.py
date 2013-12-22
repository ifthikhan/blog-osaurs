"""Main application module"""

from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET'])
def home():
    return "<h1>Blogoaurs Home</h2>"


@app.route("/<post>/<title>", methods=['GET'])
def post(title):
    return "<h2>title</h2>"


if __name__ == "__main__":
    app.run()
