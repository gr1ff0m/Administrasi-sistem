from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv

db = SQLAlchemy()


def create_app():
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{getenv('DB_USER')}:{getenv('DB_PASSWORD')}@db/{getenv('DB_NAME')}"
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.secret_key = 'randomsecret'

    db.init_app(app)

    with app.app_context():
        from . import models
        db.create_all()

        from .app import routes
        app.register_blueprint(routes)

    return app
