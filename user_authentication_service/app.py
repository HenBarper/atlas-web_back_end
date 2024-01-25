#!/usr/bin/env python3
"""Application file"""
from flask import Flask, request, jsonify
from auth import Auth

app = Flask(__name__)
AUTH = Auth()


@app.route('/', methods=['GET'], strict_slashes=False)
def get_jsonify() -> dict:
    """return a json payload"""
    return jsonify({"message": "Bienvenue"})


@app.route('/users', methods=['POST'], strict_slashes=False)
def users():
    """"""
    email = request.form.get('email')
    password = request.form.get('password')

    try:
        AUTH.register_user(email, password)
        return jsonify({"email": email, "message": "user created"}), 200
    except ValueError:
        return jsonify({"message": "email already registered"}), 400
    except Exception as e:
        return jsonify({"message": "Error occurred: {}".format(str(e))}), 500


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5000")
