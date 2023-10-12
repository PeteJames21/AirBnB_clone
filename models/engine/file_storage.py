#!/usr/bin/python3
"""
Defines a class that serializes instances to a JSON file and deserializing
a JSON file to instances.
"""

import json


class FileStorage:
    """
    Serializes and deserializes instances using JSON
    """
    __file_path = "db.json"
    __objects = {}

    def all(self):
        """Return a dict with all saved instances."""
        return self.__objects

    def new(self, obj):
        """Set in __objects the obj with key <obj class name>.id"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serialize all objects in `__objects` to a JSON file."""
        objs = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w", encoding="utf-8") as f:
            json.dump(objs, f)

    def reload(self):
        """Update the list of objects using the JSON file, if present."""
        # Placing these imports here prevents circular imports because
        # base_model.py imports file_storage, which imports base_model.
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review
        valid_classes = {
                            'Amenity', 'BaseModel', 'City', 'Place',
                            'Review', 'State', 'User'
                        }
        try:
            with open(self.__file_path, "r", encoding="utf-8") as f:
                d = json.load(f)

            for obj_dict in d.values():
                # Get the class
                cls_name = obj_dict["__class__"]
                if cls_name not in valid_classes:
                    continue

                cls = eval(cls_name)

                # Recreate the instance using its dict representation
                del obj_dict["__class__"]  # This key should not be used
                obj = cls(**obj_dict)
                # Save the instance to __objects
                self.new(obj)

        except FileNotFoundError:
            pass
