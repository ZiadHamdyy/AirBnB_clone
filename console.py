#!/usr/bin/python3
"""
This module contains the HBNBCommand class that implements.

"""

import cmd
import shlex
import json
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
from models.user import User

classes = {
        "BaseModel": BaseModel(),
        "User": User()
    }

class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that implements the command interpreter.
    """

    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel(),
        "User": User()

    }
    def do_quit(self, arg):
        """
        commend exit the program
        """
        return True

    def do_EOF(self, arg):
        """
        commend exit the program
        """
        print()
        return True

    def help_quit(self):
        """
        Help message for the quit command
        """
        print("Quit command to exit the program")

    def help_EOF(self):
        """
        Print help message for EOF command
        """
        print("Quit command to exit the program")

    def emptyline(self):
        """
        Empty line + ENTER shouldn't execute anything
        """
        print()
        pass

    def default(self, arg):
         """Handle any command that is not defined"""
         methods = {
             "all": self.do_all,
             "show": self.do_show,
             "destroy": self.do_destroy,
    }

    def do_create(self, arg):
        """
        Creates a new instance of any available model,
        and saves it...

        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            class_obj = self.classes[args[0]]
            class_obj.save()
            print(class_obj.id)

    def do_show(self, arg):
        """
        Prints the string representation
        Usage: "id"
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                print(all_objs[key])
            else:
                print("** no instance found **")
    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name.
        """
        args = shlex.split(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        else:
            all_objs = storage.all()
            key = "{}.{}".format(args[0], args[1])
            if key in all_objs:
                del all_objs[key]
                storage.save()
            else:
                print("** no instance found **")

    def do_all(self, arg):
        """
        Prints all string representation.
        """
        args = shlex.split(arg)
        all_objs = storage.all()
        if len(args) == 0:
            print([str(obj) for obj in all_objs.items()])
        elif args[0] not in self.classes:
            print("** class doesn't exist **")
        else:
            if arg[0].endswith('.all'):
                class_name = arg[0].split(".")[0]
                class_objs = [
                    value for key, value in all_objs.items()
                    if key.startswith(class_name)]
                strs = [str(obj) for obj in class_objs]
                print(strs)
            else:
                class_objs = [
                    value for key, value in all_objs.items()
                    if key.startswith(arg[0])]
                strs = [str(obj) for obj in class_objs]
                print(strs)

    def do_update(self, arg):
        """Updates an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print('** class name missing **')
            return

        class_name = args[0]

        if class_name not in self.classes:
            print('** class doesn\'t exist **')
            return

        if len(args) < 2:
            print('** instance id missing **')
            return

        instance_id = args[1]
        key = "{}.{}".format(class_name, instance_id)
        obj_dict = storage.all()

        if key not in obj_dict:
            print('** no instance found **')
            return

        if len(args) < 3:
            print('** attribute name missing **')
            return

        attribute_name = args[2]

        if len(args) < 4:
            print('** value missing **')
            return

        attribute_value = args[3].strip('"')

        instance = obj_dict[key]
        try:
            attribute_value = type(getattr(instance, attribute_name))(attribute_value)
        except (AttributeError, ValueError):
            pass

        setattr(instance, attribute_name, attribute_value)
        instance.save()
if __name__ == '__main__':
    HBNBCommand().cmdloop()
