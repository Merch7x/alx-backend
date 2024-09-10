#!/usr/bin/env python3
"""Create an instance of a flask app"""
from flask import Flask, render_template, request, g
from flask_babel import Babel
from zoneinfo import ZoneInfo
from datetime import datetime


app = Flask(__name__)


class Config:
    """Create a configuration class"""
    LANGUAGES = ["en", "fr"]
    TIMEZONE = "UTC"
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


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
    if headers:
        return headers
    return request.accept_languages.best_match(
        app.config['LANGUAGES']
    ) or app.config['BABEL_DEFAULT_LOCALE']


def get_timezone():
    """Set babel with a default timezone"""
    tz = request.args.get('timezone')
    if tz:
        try:
            pytz.timezone(tz)
            return tz
        except pytz.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']
    user = request.args.get('login_as')
    if user:
        user_tz = users.get(int(user)).get('timezone')
        try:
            pytz.timezone(user_tz)
            return user_tz
        except pytz.UnknownTimeZoneError:
            return app.config['BABEL_DEFAULT_TIMEZONE']

    return app.config['BABEL_DEFAULT_TIMEZONE']


babel = Babel(app, locale_selector=get_locale, timezone_selector=get_timezone)


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
    g.user = get_user()


@app.route('/')
def index():
    """Define an index route"""
    username = g.user['name'] if g.user else None
    user_tz = g.user['timezone'] if g.user else None
    t_now = datetime.now(ZoneInfo(user_tz))
    current_time = t_now.strftime('%b %d, %Y, %I:%M:%S')
    return render_template("index.html",
                           username=username,
                           current_time=current_time)
