#!/usr/bin/python3
"""
This module contains the BaseModel class.
"""
import uuid
import datetime
from models import storage


class BaseModel:
    """
This class will be the 'base' of all other classes in this project.
The goal of it is to manage id attribute in all future classes and
to avoid duplicating the same code (by extension, same bugs).
"""
    def __init__(self, *args, **kwargs):
        """
        This method initializes a new created BaseModel object.
        """
        self.id = str(uuid.uuid4())
        if args is not None and len(args) > 0:
            pass
        elif (kwargs is None or len(kwargs) == 0):
            self.created_at = datetime.datetime.now()
            self.updated_at = datetime.datetime.now()
            storage.new(self)
        else:
            for key in kwargs:
                if key == '__class__':
                    pass
                elif key == 'created_at' or key == 'updated_at':
                    self.__dict__[key] = datetime.datetime.fromisoformat(
                        kwargs[key])
                else:
                    self.__dict__[key] = kwargs[key]

    def __str__(self):
        """
    This class method provides the informal string representation of BaseModel.
        """
        if self.id is None:
            return "[{}] ({}) {}".format(self.__class__.__name__)
        my_str = "[{}] ({}) {}".format(
                        self.__class__.__name__,
                        self.id,
                        self.__dict__)
        return my_str

    def save(self):
        """
This public instance method updates the public instance
attribute updated_at with the current datetime.
    """
        self.updated_at = datetime.datetime.now()
        storage.new(self)
        storage.save()

    def to_dict(self):
        """
    This public instance method returns returns a dictionary
    containing all keys/values of __dict__ of the instance.
        """
        my_dict = {}
        my_dict.update(self.__dict__)
        my_dict['__class__'] = self.__class__.__name__
        my_dict['created_at'] = self.created_at.isoformat()
        my_dict['updated_at'] = self.updated_at.isoformat()
        return my_dict
