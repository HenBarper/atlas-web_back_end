#!/usr/bin/env python3
"""Create a new Flask view that handles
all routes for the Session authentication"""
from api.v1.views import app_views
from flask import request, jsonify
from models.user import User


@app_views.route('/auth_session/login', methods=['POST'], strict_slashes=False)
def login_method():
    """Method to login"""
    email = request.form.get(request.email)
    if not email:
        return jsonify({ "error": "email missing" }, 400)
    pwd = request.form.get(request.password)
    if not pwd:
        return jsonify({ "error": "password missing" }, 400)
    user = User.search(email)
    if not user:
        return jsonify({ "error": "no user found for this email" }, 404)
    if not user.is_valid_password(pwd):
        return jsonify({ "error": "wrong password" }, 401)
    else:
        from api.v1.app import auth
        session_id = auth.create_session()
        return (User(session_id)).to_json()
    
