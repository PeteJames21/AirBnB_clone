#!/usr/bin/python3
"""
Defines a class that models a state (residence location) of a user.
"""
from .base_model import BaseModel


class State(BaseModel):
    """Models a state."""
    name = ""
