#!/usr/bin/python3

from datetime import datetime
from . import storage
import uuid


class BaseModel:
    '''Defines all common attributes/methods for other classes'''
    def __init__(self, *args, **kwargs):
        '''
        This is the constructor of the base model

        *args is unused;
        if **kwargs is not empty, it re-creates an instance with
        the dictionary representation
        else, a new instance is created
        '''
        date_format = "%Y-%m-%dT%H:%M:%S.%f"
        self.id = str(uuid.uuid4())
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key in ('created_at', 'updated_at'):
                    self.__dict__[key] = datetime.strptime(value, date_format)
                else:
                    self.__dict__[key] = value
        else:
            self.created_at = datetime.now()
            self.updated_at = self.created_at
            storage.new(self)

    def save(self):
        '''updates the public instance attribute updated_at
            with the current datetime'''
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        '''
        Returns a dictionary containing all keys/values of
        __dict__ of the instance:

        A key __class__ contains the class name of the object
        '''
        obj_dict = self.__dict__.copy()
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        obj_dict["__class__"] = self.__class__.__name__
        return obj_dict

    def __str__(self):
        return ("[{}] ({}) {}".format(self.__class__.__name__, self.id,
                self.__dict__))
