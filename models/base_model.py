#!/usr/bin/python3
"""
Define a BaseModel class that defines all common attributes/methods
for other classes.
"""


class BaseModel:
    """A base class for all other classes."""

    def __init__(self, *args, **kwargs):
        self.id = ...
        self.created_at = ...
        self.updated_at = ...

    def save(self):
        raise NotImplementedError

    def to_dict(self):
        raise NotImplementedError

    def __str__(self):
        raise NotImplementedError
