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
    user = request.args.get('login_as')
    if user:
        lang = users.get(int(user)).get('locale')
        if lang in app.config['LANGUAGES']:
            return lang
    headers = request.headers.get("locale")
    if headers and headers in app.config['LANGUAGES']:
        return headers
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
    user_id = request.args.get('login_as')

    if user_id is None:
        return None

    try:
        user_id = int(user_id)
    except ValueError:
        return None

    user = users.get(user_id)

    if user is None:
        return None

    return user


@app.before_request
def before_request():
    """Execute before every request"""
    user = get_user()
    g.user = user['name'] if user else None


@app.route('/')
def index():
    """Define an index route"""
    username = g.user
    return render_template("5-index.html", username=username)
