#!/usr/bin/env python3
"""Create an instance of a flask app"""
from flask import Flask, render_template, request
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


@babel.localeselector
def get_locale():
    """Selects a locale for babel"""
    locale = request.args.get('locale')
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    ) or app.config['BABEL_DEFAULT_LOCALE']


@app.route('/')
def index():
    """Define an index route"""
    return render_template("2-index.html")
