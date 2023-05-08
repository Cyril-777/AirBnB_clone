#!/usr/bin/python3
"""BaseModel parent class that contains all common attributes/methods for other classes"""

import uuid
from datetime import datetime
import models

class BaseModel:
    def __init__(self, *args, **kwargs):
        """Class constructor that receives all the arguments and sets
        the 'created_at', 'updated_at', 'deleted_at' and 'id' attributes"""
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key == 'created_at' or key == 'updated_at':
                        value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = self.created_at

    def __str__(self):
        """String representation of the object"""
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)

    def save(self):
        """Method that saves the current instance to the new_dicbase"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """dict representation of the object"""
        new_dic = self.__dict__.copy()
        new_dic["__class__"] = self.__class__.__name__
        new_dic["created_at"] = self.created_at.isoformat()
        new_dic["updated_at"] = self.updated_at.isoformat()
        return new_dic