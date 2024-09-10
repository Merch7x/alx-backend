#!/usr/bin/env python3
"""Create an instance of a flask app"""
from flask import Flask, render_template, request
from flask_babel import Babel
app = Flask(__name__)
babel = Babel(app)


class Config:
    """Create a configuration class"""
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"


# app.config.from_object(Config)
babel = Babel(app, default_timezone=Config.TIMEZONE,
              default_locale=Config.LANGUAGES[0])


@app.route('/')
def index():
    """Define an index route"""
    return render_template("0-index.html")
