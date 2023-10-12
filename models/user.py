#!/usr/bin/python3
"""
Models an AirBnB user.
"""
from .base_model import BaseModel


class User(BaseModel):
    """Models an AirBnB user."""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
