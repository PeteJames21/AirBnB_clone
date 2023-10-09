#!/usr/bin/python3
"""
Defines a class serializes instances to a JSON file and deserializing
a JSON file to instances.
"""


class FileStorage:
    """
    Serializes and deserializes instances using JSON
    """
    __file_path = ...
    __objects = ...

    def __init__(self):
        pass

    def all(self):
        raise NotImplementedError

    def new(self, obj):
        raise NotImplementedError

    def save(self):
        raise NotImplementedError

    def reload(self):
        raise NotImplementedError
