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
        '''Empty line + enter does nothing'''
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
        '''Prints the string representation of a given class'''
        if not arg:
            instances = storage.all().values()
        else:
            if not class_name_is_valid(arg):
                return
            class_name = arg
            class_instances = storage.all().values()
            instances = []
            for instance in class_instances:
                if instance.__class__.__name__ == class_name:
                    instances.append(str(instance))
        if instances:
            print(instances)

    def do_update(self, arg):
        raise NotImplementedError

    def do_EOF(self, arg):
        '''Ctrl+Z to quits the program'''
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
