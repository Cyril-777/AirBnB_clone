#!/usr/bin/python3

import json
import models


class FileStorage:
    """
    most simple implementation of storage,
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
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file"""
        serialized_objects = {}
        for key, obj in self.__objects.items():
            serialized_objects[key] = obj.to_dict()
        with open(self.__file_path, mode='w', encoding="UTF8") as json_file:
            json.dump(serialized_objects, json_file)

    def reload(self):
        """Deserializes the JSON file to __objects"""
        try:
            with open(self.__file_path, mode='r', encoding="UTF8") as json_file:
                self.__objects = json.load(json_file)
            for key, obj in self.__objects.items():
                class_name = obj["__class__"]
                class_name = models.classes[class_name]
                self.__objects[key] = class_name(**obj)
        except FileNotFoundError:
            pass
