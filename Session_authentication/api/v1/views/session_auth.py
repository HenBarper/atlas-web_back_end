#!/usr/bin/env python3
"""Create a new Flask view that handles
all routes for the Session authentication"""
from flask import request, jsonify
from api.v1.views import app_views
from models.user import User
import os


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Method to login"""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}, 400)
    pwd = request.form.get('password')
    if not pwd:
        return jsonify({"error": "password missing"}, 400)

    user = User()
    user_email = user.search({'email': email})
    if not user_email:
        return jsonify({"error": "no user found for this email"}, 404)
    if not user.is_valid_password(pwd):
        return jsonify({"error": "wrong password"}, 401)

    from api.v1.app import auth
    session_id = auth.create_session(user.id)
    dictionary = user_email.to_json()

    response = jsonify(dictionary)
    response.set_cookie(os.getenv('SESSION_NAME'), session_id)

    return response
