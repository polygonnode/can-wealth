
from flask import Flask                     #import flask module
from app.views.home import home
from app.views.planner import planner

def create_app():
    app = Flask(__name__)

    app.config.update(
        DEBUG = True,
        SECRET_KEY = 'secret_xxx'
    )
    #register blue prints
    app.register_blueprint(home)
    app.register_blueprint(planner)

    return app
