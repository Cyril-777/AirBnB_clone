#!/usr/bin/python3
"""storage json file"""
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
import os.path
import json


class FileStorage:
    """
    The most simple implementation of storage,
    which stores data in a flat file
    serializes instances to a JSON file
    and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = str(obj.__class__.__name__) + "." + str(obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, mode='w', encoding="UTF8") as js_f:
            json.dump(serialized_objects, js_f)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        if os.path.isfile(self.__file_path):
            with open(self.__file_path, "r", encoding="utf-8") as js_f:
                for key, obj in json.loads(js_f.read()).items():
                    obj = eval(obj['__class__'])(**obj)
                    self.__objects[key] = obj
