#!/usr/bin/python3
"""The entry point of the command line interpreter"""

import cmd
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity
from models import storage
import models
import json


class HBNBCommand(cmd.Cmd):
    """HBNB Command line interpreter"""
    prompt = "(hbnb) "
    v_classes = ["BaseModel", "User", "Place", "State\
", "City", "Amenity", "Review"]  # valid classes

    def do_quit(self, args):
        """Quit command to exit the console"""
        return True

    def do_EOF(self, args):
        """EOF command to exit the console"""
        return True

    def emptyline(self):
        """emptyline - shouldnt execute anything when given no commands"""
        pass

    def do_create(self, line):
        """Creates a new instance of BaseModel, saves it, and print the id"""
        if not line:
            print("** class name missing **")
            return
        elif line not in HBNBCommand.v_classes:
            print("** class doesn't exist **")
            return
        else:
            new_ins = eval(line)()
            new_ins.save()
            print(new_ins.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        if not line:
            print("** class name missing **")
            return
        args = line.split(' ')
        if args[0] not in HBNBCommand.v_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            print(storage.all()[key])
        else:
            print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split(' ')
        if args[0] not in HBNBCommand.v_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key in storage.all():
            del storage.all()[key]
            storage.save()
        else:
            print("** no instance found **")

    def do_all(self, line):
        """Prints all string representation of all instances"""
        if line:
            args = line.split(' ')
            if args[0] not in HBNBCommand.v_classes:
                print("** class doesn't exist **")
                return
            else:
                result = [str(obj) for obj in storage.all().values()
                        if isinstance(obj, eval(args[0]))]
                print(', '.join(result))
        else:
            result = [str(obj) for obj in storage.all().values()]
            print(', '.join(result))

    def do_update(self, line):
        """Updates an instance based on the class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.v_classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        instance_id = args[1]
        key = "{}.{}".format(args[0], instance_id)
        if key not in storage.all():
            print("** no instance found **")
            return
        if len(args) < 3:
            print("** attribute name missing **")
            return
        if len(args) < 4:
            print("** value missing **")
            return
        attr_name = args[2]
        attr_value = args[3]
        obj = storage.all()[key]
        if hasattr(obj, attr_name):
            attr_type = type(getattr(obj, attr_name))
            try:
                if attr_value.startswith('"') and attr_value.endswith('"'):
                    attr_value = attr_value.strip('"')
                casted_value = attr_type(attr_value)
                setattr(obj, attr_name, casted_value)
                obj.save()
            except ValueError:
                print("** value missing **")

    def do_count(self, line):
        """retrieve the number of instances of a class"""
        if not line:
            print("** class name missing **")
            return
        args = line.split(' ')
        if args[0] not in HBNBCommand.v_classes:
            print("** class doesn't exist **")
            return
        count = 0
        for obj in storage.all().values():
            if isinstance(obj, eval(args[0])):
                count += 1
        print(count)

    def default(self, line):
        """Default method to handle advanced commands"""
        args = line.split('.')
        if len(args) < 2:
            print("** no instance found **")
            return
        cn = args[0]  # class name
        if cn not in HBNBCommand.v_classes:
            print("** no instance found **")
            return
        command = args[1].split('(')[0]
        if command == "all":
            self.do_all(cn)
        elif command == "count":
            self.do_count(cn)
        elif command == "show":
            ins_id = args[1].split('"')[1]
            self.do_show("{} {}".format(cn, ins_id))
        elif command == "destroy":
            ins_id = args[1].split('"')[1]
            self.do_destroy("{} {}".format(cn, ins_id))
        elif command == "update":
            update_args = args[1].split('(')[1].split(')')[0].replace('"', '').split(', ')
            ins_id = update_args[0]
            att_n = update_args[1]
            att_v = update_args[2]
            self.do_update("{} {} {} {}".format(cn, ins_id, att_n, att_v))
        else:
            print("** no instance found **")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
