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


def is_valid(hashed_password: bytes, password: str) -> bool:
    """This fuction uses bcrypt to validate that
    the provided password matches the hashed password"""
    password = password.encode('utf-8')
    return bcrypt.checkpw(password, hashed_password)
