#!/usr/bin/python3
"""
Contains the entry point of the command interpreter.
"""
import cmd
from models import storage
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
import re
import shlex
import json


valid_classes = {
                    'Amenity', 'BaseModel', 'City', 'Place',
                    'Review', 'State', 'User'
                }


def class_name_is_valid(class_name):
    """Return True if class_name is valid, else False."""
    if not class_name:
        print("** class name missing **")
        return False
    elif class_name not in valid_classes:
        print("** class doesn't exist **")
        return False
    return True


def id_exists(obj_id):
    """Return True if the object id exists, else False"""
    try:
        storage.all()[obj_id]
        return True
    except KeyError:
        print("** no instance found **")
        return False


class HBNBCommand(cmd.Cmd):
    """The console command interpreter."""
    prompt = "(hbnb) "

    def emptyline(self):
        """Empty line + enter does nothing."""
        pass

    def do_quit(self, arg):
        '''Quit exits the program'''
        return True

    def do_create(self, arg):
        """Create and save an instance of the class in arg and print its id."""
        if not class_name_is_valid(arg):
            return

        # Create an instance of the class and save it
        obj = eval(arg)()
        obj.save()
        print(obj.id)

    def do_show(self, arg):
        """Print an instance based on its class name and ID."""
        args = [""] * 2
        i = 0
        for arg_ in arg.split():
            args[i] = arg_
            i += 1
            if i >= 2:
                break

        if not class_name_is_valid(args[0]):
            return
        if not args[1]:
            print("** instance id missing **")
            return

        id_ = ".".join(args)
        if not id_exists(id_):
            return
        obj = storage.all()[id_]
        print(obj)

    def do_destroy(self, arg):
        """Destroy an instance based on its class name and ID."""
        args = [""] * 2
        i = 0
        for arg_ in arg.split():
            args[i] = arg_
            i += 1
            if i >= 2:
                break

        if not class_name_is_valid(args[0]):
            return
        if not args[1]:
            print("** instance id missing **")
            return

        id_ = ".".join(args)
        if not id_exists(id_):
            return

        # Destroy the instance
        del storage.all()[id_]
        storage.save()

    def do_all(self, arg):
        """Print the string representation of all instances of a class."""
        if not arg:
            instances = storage.all().values()
        else:
            if not class_name_is_valid(arg):
                return
            class_name = arg
            instances = [
                        instance for instance in storage.all().values()
                        if instance.__class__.__name__ == class_name]
        if instances:
            print([str(instance) for instance in instances])

    def do_update(self, arg):
        """Update an instance based on the class name and id."""
        tokens = shlex.split(arg)

        if len(tokens) == 0:
            print("** class name missing **")
            return
        elif tokens[0] not in valid_classes:
            print("** class doesn't exist **")
            return
        elif len(tokens) == 1:
            print("** instance id missing **")
            return

        object_id = tokens[0] + "." + tokens[1]
        if not id_exists(object_id):
            return
        if len(tokens) == 2:
            print("** attribute name missing **")
            return
        elif len(tokens) == 3:
            print("** value missing **")
            return
        else:
            instance = storage.all()[object_id]
            setattr(instance, tokens[2], tokens[3])
            instance.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class."""
        if not class_name_is_valid(arg):
            return
        count = 0
        all_objects = storage.all()

        for key, value in all_objects.items():
            class_name = key.split('.')
            if class_name[0] == arg:
                count += 1
        print(count)

    def default(self, arg):
        """
        Execute commands of the form className.cmdName(*args).

        An error is printed if the syntax does not match the above or if the
        syntax is correct but the command name does not exist.
        """
        cmd_table = {
            "all": self.do_all, "count": self.do_count,
            "create": self.do_create, "show": self.do_show,
            "destroy": self.do_destroy, "update": self.do_update
        }

        # Extract the class name, command name, and arguments
        pattern = (r"\A(?P<className>\w+?)\.(?P<cmd>\w+?)\((?P<args>.*?)"
                   r"(?P<dict>\{.*?\})?\)\Z")
        parser = re.compile(pattern)
        result = parser.match(arg)
        if not result:
            print(f"*** Unknown syntax: {arg}")
            return
        class_name, cmd_name, args, arg_dict = result.groups()
        if cmd_name not in cmd_table.keys():
            print(f"*** Unknown syntax: {cmd_name}")
            return

        # Strip quotes from args, e.g. 'a, "b", c' -> 'a b c'
        arg_pattern = re.compile('[^,"\']+')
        args = arg_pattern.findall(args)
        args = " ".join([arg.strip() for arg in args if not arg.isspace()])
        n_args = len(args.split())

        # Allow 'update' to be called with the syntax:
        # 'clsName.update(id, {key: value...})'
        if arg_dict and cmd_name == "update":
            if n_args > 1:
                print("*** Error in <update>: too many arguments")
                return
            if not id_exists(f"{class_name}.{args}"):
                return

            try:
                d = json.loads(arg_dict.replace("'", "\""))
                for key, value in d.items():
                    self.onecmd(f"update {class_name} {args} {key} {value}")

            except json.decoder.JSONDecodeError:
                print(f"*** Invalid dict representation: {arg_dict}")

        else:
            self.onecmd(f"{cmd_name} {class_name} {args}")

    def do_EOF(self, arg):
        """Ctrl+Z to quit the program."""
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
