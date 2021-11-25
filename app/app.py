from flask import Flask
from flask_cors import CORS


def create_app():
    app = Flask(__name__)

    # CORS
    CORS(app)

    # Config
    app.config.from_pyfile("config.py")

    return app
