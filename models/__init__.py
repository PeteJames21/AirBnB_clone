#!/usr/bin/python3
"""
This module creates an instance for managing all JSON database-related
operations across the entire project. There should be only one FileStorage
instance during the program's lifetime and it should be created here.
"""
from engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
