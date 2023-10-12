#!/usr/bin/python3
"""
Defines a class that models a city.
"""
from .base_model import BaseModel


class City(BaseModel):
    """Models a city."""
    state_id = ""
    name = ""
