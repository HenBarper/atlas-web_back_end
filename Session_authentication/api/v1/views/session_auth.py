#!/usr/bin/env python3
"""Create a new Flask view that handles
all routes for the Session authentication"""
from flask import request, jsonify, make_response
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

    user = User.search({'email': email})
    if not user:
        return jsonify({"error": "no user found for this email"}, 404)
    if not user.is_valid_password(pwd):
        return jsonify({"error": "wrong password"}, 401)

    from api.v1.app import auth
    user_dict = user.to_json()

    session_id = auth.create_session(user.id)
    session_cookie_name = os.getenv('SESSION_NAME')
    response = jsonify(user_dict)
    response = make_response(response)

    response.set_cookie(session_cookie_name, session_id)

    return response
