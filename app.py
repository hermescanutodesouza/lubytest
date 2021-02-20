from flask import Flask
from flask_marshmallow import Marshmallow
from flask_sqlalchemy import SQLAlchemy

from config.config import Config

db = SQLAlchemy()
ma = Marshmallow()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config())
    db.init_app(app)
    db.create_all(app=app)
    return app


def getMarshmallow(app):
    ma = Marshmallow(app)
    return ma
