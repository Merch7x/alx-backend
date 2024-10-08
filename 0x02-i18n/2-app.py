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
babel = Babel(app, default_timezone=app.config['TIMEZONE'])


@babel.localeselector
def get_locale():
    """Selects a locale for babel"""
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    )


@app.route('/')
def index():
    """Define an index route"""
    return render_template("2-index.html")
