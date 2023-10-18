#!/usr/bin/python3
"""
This module contains the FileStorage class.
"""
import json
import os
import datetime


class FileStorage:
    """
This class serializes instances to a JSON file
and deserializes JSON file to instances.
"""
    __file_path = "file.json"
    __objects = dict()

    def __init__(self):
        """
This method initializes a new created FileStorage object.
"""

    def all(self):
        """
This method returns the dictionary __objects.
"""
        return FileStorage.__objects

    def new(self, obj):
        """
        This method sets in __objects the obj with key
        <obj class name>.id
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        This method serializes __objects to the JSON file
        (path: __file_path)
        """
        my_dict = {}
        for key in FileStorage.__objects:
            my_dict[key] = FileStorage.__objects[key].to_dict()
        data = json.dumps(my_dict)
        with open(FileStorage.__file_path, "w") as f:
            f.write(data)

    def reload(self):
        """
This method deserializes the JSON file to __objects
only if the JSON file (__file_path) exists ;
otherwise, do nothing. If the file doesn’t exist,
no exception should be raised)
"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.place import Place
        from models.amenity import Amenity
        from models.review import Review
        text = ""
        file_name = FileStorage.__file_path
        if not os.path.isfile(file_name):
            return None
        with open(file_name, "r") as f:
            text = f.read()
        json_dict = json.loads(text)
        for key in json_dict:
            new_obj = eval("{}(**json_dict[key])".format(
                json_dict[key]['__class__']))
            json_dict[key] = new_obj
        FileStorage.__objects.update(json_dict)
