#!/usr/bin/python3
"""
5. Store first object
"""

import json
import os
import models
from models.bsse_model import BaseModel


class FileStorage:
    """
    serializes instances to a JSON file and
    deserializes JSON file to instances
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """

        return self.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key
        <obj class name>.id
        """

        if obj:
            self.__objects["{}.{}".format(
                obj.__class__.__name__, obj.id)] = obj

    def save(self):
        """
        serializes __objects to the JSON
        file (path: __file_path)
        """
        new_dict = {}
        for id, object in self.__objects.items():
            new_dict[id] = object.to_dict()
        with open(self.__file_path, mode="w", encoding="UTF-8") as myfile:
            json.dump(new_dict, myfile)

    def reload(self):
        """
        deserializes the JSON file to __objects
        (only if the JSON file (__file_path) exists
        """
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, mode="r", encoding="UTF-8") as myfile:
                python_dict = json.loads(myfile.read())
                my_dict = {"BaseModel": BaseModel}
                for key, val in python_dict.items():
                    obj_type = key.split(".", 1)[0]
                    self.new(my_dict[obj_type](**val))
