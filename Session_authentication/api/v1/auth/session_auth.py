#!/usr/bin/env python3
"""This class is the template
for all session authentication
system you will implement."""
from api.v1.auth.auth import Auth
import uuid


class SessionAuth(Auth):
    """Session auth class"""
    user_id_by_session_id  = {}

    def create_session(self, user_id: str = None) -> str:
        """creates a Session ID for a user_id"""
        if user_id is None or not isinstance(user_id, str):
            return None
        else:
            session_id = uuid.uuid4()
            SessionAuth.user_id_by_session_id[session_id] = user_id
            return session_id
