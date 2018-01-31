
from flask import Flask                     #import flask module
from app.views.home import home
from app.views.planner import planner

from app.models import db

def create_app():
    app = Flask(__name__)

    app.config.update(
        DEBUG = True,
        SECRET_KEY = 'secret_xxx'
    )

    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.sqlite'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    db.init_app(app)
    #register blue prints
    app.register_blueprint(home)
    app.register_blueprint(planner)


    return app
