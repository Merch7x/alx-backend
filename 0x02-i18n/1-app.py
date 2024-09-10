#!/usr/bin/env python3
"""Create an instance of a flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """Create a configuration class"""
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


app.config.from_object(Config)
app.config['BABEL_DEFAULT_LOCALE'] = app.config['LANGUAGES'][0]
app.config['BABEL_DEFAULT_TIMEZONE'] = app.config['TIMEZONE']
babel = Babel(app, default_locale=app.config['LANGUAGES'][0],
              default_timezone=app.config['TIMEZONE'])


@app.route('/')
def index():
    """Define an index route"""
    return render_template("1-index.html")
