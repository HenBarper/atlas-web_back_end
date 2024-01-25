#!/usr/bin/env python3
"""Authorization file!"""
import bcrypt


def _hash_password(password: str) -> bytes:
    """takes in a password string arguments and returns bytes"""
    hash_pass = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hash_pass
