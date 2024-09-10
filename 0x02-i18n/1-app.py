#!/usr/bin/env python3
"""Create an instance of a flask app"""
from flask import Flask, render_template
from flask_babel import Babel
app = Flask(__name__)


class Config:
    """Create a configuration class"""
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
babel = Babel(app)


@app.route('/')
def index():
    """Define an index route"""
    return render_template("1-index.html")
