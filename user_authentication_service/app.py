#!/usr/bin/env python3
"""Application file"""
from flask import Flask, request, jsonify
# from auth import Auth

app = Flask(__name__)
# AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def get_jsonify() -> dict:
    """return a json payload"""
    return jsonify({"message": "Bienvenue"})


# @app.route('/users', methods=['POST'], strict_slashes=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
