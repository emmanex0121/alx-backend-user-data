#!/usr/bin/env python3
""" Module of Auth
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """ Class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method require auth of bool retun type """

        if not path or not excluded_paths:
            return True
        if not path[-1] == "/":
                path = path + "/"
        if path in excluded_paths:
            return False
        return True
        # if path is None or excluded_paths

    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""
        return None
