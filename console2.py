#!/usr/bin/python3

import cmd
import sys
from models.engine.file_storage import FileStorage
from models.base_model import BaseModel
from models.user import User

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        """Do nothing on empty line + ENTER."""
        pass

    def do_quit(self, arg):
        """Exit the command interpreter."""
        sys.exit()

    def do_EOF(self, arg):
        """Exit the command interpreter."""
        print()
        sys.exit()

    def do_create(self, arg):
        """Create a new instance of BaseModel, save it, and print the id."""
        if not arg:
            print("** class name missing **")
            return

        try:
            # Dynamically create an instance of the specified class
            cls = eval(arg)  # Note: Using eval can have security implications
            new_instance = cls()
            new_instance.save()
            print(new_instance.id)

        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Print the string representation of an instance."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        try:
            cls = eval(args[0])
            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_id = args[1]
            key = "{}.{}".format(cls.__name__, obj_id)
            all_objects = storage.all()

            if key in all_objects:
                print(all_objects[key])
            else:
                print("** no instance found **")

        except NameError:
            print("** class doesn't exist **")

    def do_destroy(self, arg):
        """Delete an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        try:
            cls = eval(args[0])
            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_id = args[1]
            key = "{}.{}".format(cls.__name__, obj_id)
            all_objects = storage.all()

            if key in all_objects:
                del all_objects[key]
                storage.save()
            else:
                print("** no instance found **")

        except NameError:
            print("** class doesn't exist **")

    def do_all(self, arg):
        """Print string representation of all instances."""
        args = arg.split()
        all_objects = storage.all()

        if not arg:
            print([str(obj) for obj in all_objects.values()])
        else:
            try:
                cls = eval(args[0])
                print([str(obj) for key, obj in all_objects.items() if key.startswith(cls.__name__)])
            except NameError:
                print("** class doesn't exist **")

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        if not arg:
            print("** class name missing **")
            return

        args = arg.split()
        try:
            cls = eval(args[0])
            if len(args) < 2:
                print("** instance id missing **")
                return

            obj_id = args[1]
            key = "{}.{}".format(cls.__name__, obj_id)
            all_objects = storage.all()

            if key in all_objects:
                if len(args) < 3:
                    print("** attribute name missing **")
                elif len(args) < 4:
                    print("** value missing **")
                else:
                    attribute_name = args[2]
                    attribute_value = args[3]

                    # Update the attribute value
                    setattr(all_objects[key], attribute_name, eval(attribute_value))
                    storage.save()

            else:
                print("** no instance found **")

        except NameError:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()

