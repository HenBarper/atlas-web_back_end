#!/usr/bin/env python3
"""2-app.y file"""
from flask import Flask, render_template, request
from flask_babel import Babel


app = Flask(__name__)
babel = Babel(app)


class Config:
    """Configuration class"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale():
    """function to get user locale"""
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """initial route to index"""
    return render_template('2-index.html')


if __name__ == '__main__':
    app.run(debug=True)
