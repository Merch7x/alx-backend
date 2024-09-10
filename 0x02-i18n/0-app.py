#!/usr/bin/env python3
"""Create an instance of a flask app"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """Define an index route"""
    return render_template("0-index.html")
