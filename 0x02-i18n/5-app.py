#!/usr/bin/env python3
"""Create an instance of a flask app"""
from flask import Flask, render_template, request, g
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


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user():
    """Retrieves a user from a list"""
    user_id = request.args.get('login_as', type=int)
    if user_id is not None:
        return users.get(user_id)
    return None


@app.before_request
def before_request():
    """Execute before every request"""
    g.user = get_user()


@app.route('/')
def index():
    """Define an index route"""
    user = g.user
    return render_template("5-index.html", user=user)
