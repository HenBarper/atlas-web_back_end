#!/usr/bin/env python3
"""This class is the template
for all authentication system
you will implement."""
from flask import request
from typing import List, TypeVar


class Auth:
    """class to manage the API authentication"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """returns false"""
        return False

    def authorization_header(self, request=None) -> str:
        """returns none"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """returns none"""
        return None
