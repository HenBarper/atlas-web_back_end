#!/usr/bin/env python3
"""User passwords should NEVER be
stored in plain text in a database"""
import bcrypt


def hash_password(password: str) -> bytes:
    """function that expects one string argument
    name password and returns a salted, hashed
    password, which is a byte string"""
    password = password.encode('utf-8')
    return bcrypt.hashpw(password, bcrypt.gensalt())
