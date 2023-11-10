#!/usr/bin/python3
"""
This module contains the HBNBCommand class that implements.

"""

import cmd
import shlex
from models.base_model import BaseModel
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """
    HBNBCommand class that implements the command interpreter.
   
    """
    prompt = "(hbnb) "
    classes = {
        "BaseModel": BaseModel(),
        "User": User(),
        "State": State(),
        "City": City(),
        "Amenity": Amenity(),
        "Place": Place(),
        "Review": Review()
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

    def emptyline(self):
        """
        Empty line + ENTER shouldn't execute anything
        """
        pass

if __name__ == '__main__':
    HBNBCommand().cmdloop()

    def default(self, arg):
         """Handle any command that is not defined"""
         methods = {
             "all": self.do_all,
             "show": self.do_show,
             "destroy": self.do_destroy,
             "count": self.do_count,
             "update": self.do_update
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
