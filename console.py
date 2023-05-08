#!/usr/bin/python3
"""The entry point of the command line interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.place import Place
from models.city import City
from models.review import Review
from models.amenity import Amenity
import models
import json


class HBNBCommand(cmd.Cmd):
    """HBNB Command line interpreter"""
    prompt = "(hbnb) "

    def do_quit(self, args):
        """Quit command to exit the console"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the console"""
        return True

    def emptyline(self):
        """emptyline - shouldnt execute anything when given no commands"""
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()