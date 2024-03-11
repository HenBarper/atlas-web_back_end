#!/usr/bin/env python3
"""Authorization file!"""
import bcrypt
from db import DB
from user import User
from sqlalchemy.exc import ValueError


class Auth:
    """Auth class to interact with the authentication database.
    """
    def __init__(self):
        self._db = DB()

    def register_user(self, email: str, password: str) -> User:
        """take mandatory email and password
        string arguments and return a User"""
        if self._db.find_user_by(email=email):
            raise ValueError(f'User {email} already exits')
        hash = self._hash_password(password)
        new_user = self._db.add_user(email, hash)
        return new_user

    def _hash_password(self, password: str) -> bytes:
        """takes in a password string arguments and returns bytes"""
        hash_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        return hash_pass


def _hash_password(self, password: str) -> bytes:
    """takes in a password string arguments and returns bytes"""
    hash_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hash_pass
