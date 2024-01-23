#!/usr/bin/env python3
"""Create a new Flask view that handles
all routes for the Session authentication"""
from api.v1.views import app_views
from flask import request, jsonify
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login():
    """Route for session authentication"""
    email = request.form.get('email')
    if not email:
        return jsonify({"error": "email missing"}), 400

    password = request.form.get('password')
    if not password:
        return jsonify({"error": "password missing"}), 400

    users = User.search({"email": email})
    if not users:
        return jsonify({"error": "no user found for this email"}), 404

    user = users[0]
    if not user.is_valid_password(password):
        return jsonify({"error": "wrong password"}), 401

    user_dict = user.to_json()

    session_id = auth.create_session(user.id)
    session_cookie_name = os.getenv('SESSION_NAME')
    response = jsonify(user_dict)
    response = make_response(response)

    response.set_cookie(session_cookie_name, session_id)

    return response
