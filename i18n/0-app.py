#!/usr/bin/env python3
"""0-app.y file"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    """initial route to index"""
    return render_template('/templates/index.html')
