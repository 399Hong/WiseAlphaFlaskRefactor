import pathlib

import sqlite3
from flask import Flask, jsonify, request
import utils


def create_app(test_config = None):

    app = Flask(__name__)

    if test_config is None:
        app.config.from_object("config.Config")
    else:
        app.config.from_mapping(test_config)
        
    with app.app_context():
        from .widget import widget
        app.register_blueprint(widget.widget_blueprint)
        from .home import home
        app.register_blueprint(home.home_blueprint)

    return app
