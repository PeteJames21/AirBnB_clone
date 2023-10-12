#!/usr/bin/python3
"""
Defines a class that models an AirBnB review.
"""
from .base_model import BaseModel


class Review(BaseModel):
    """Models an AirBnB review."""
    place_id = ""
    user_id = ""
    text = ""
