#!/usr/bin/env python3
""" Module of Auth
"""
from flask import request
from typing import TypeVar, List


class Auth:
    """ Class Auth """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Public method require auth of bool retun type """
        return False
    
    def authorization_header(self, request=None) -> str:
        """Returns None"""
        return None
    
    def current_user(self, request=None) -> TypeVar('User'):
        """Return None"""
        return None