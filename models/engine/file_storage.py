#!/usr/bin/python3
"""
This module contains the FileStorage class.
"""
import json
import os


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
        FileStorage.__objects[key] = obj.to_dict()

    def save(self):
        """
        This method serializes __objects to the JSON file
        (path: __file_path)
        """
        data = json.dumps(FileStorage.__objects)
        with open(FileStorage.__file_path, "w") as f:
            f.write(data)

    def reload(self):
        """
This method deserializes the JSON file to __objects
only if the JSON file (__file_path) exists ;
otherwise, do nothing. If the file doesn’t exist,
no exception should be raised)
"""
        text = ""
        file_name = FileStorage.__file_path
        if not os.path.isfile(file_name):
            return None
        with open(file_name, "r") as f:
            text = f.read()
        json_dict = json.loads(text)
        FileStorage.__objects.update(json_dict)
