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
            instances = [
                        instance for instance in storage.all().values()
                        if instance.__class__.__name__ == class_name]
        if instances:
            print([str(instance) for instance in instances])

    def do_update(self, arg):
        '''Updates an instance based on the class name and id'''
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
        '''Retrieves the number of instances of a class'''
        if not class_name_is_valid(arg):
            return
        count = 0
        all_objects = storage.all()
        '''
        <classname.id>:<memory location>
        '''
        for key, value in all_objects.items():
            class_name = key.split('.')
            if class_name[0] == arg:
                count += 1
        print(count)
    
    def default(self, arg):
        class_name, all_commands = arg.split(".", 1)
        command_list = all_commands.split("(")
        command = command_list[0]
        if command == 'count':
            self.onecmd(f'count {class_name}')
        
        if command == 'all':
            self.onecmd(f'all {class_name}')
        
        #get id
        pattern = r'"([^"]*)"'
        id_list = re.findall(pattern, arg)
        id = id_list[0]

        if command == 'show':
            self.onecmd(f'show {class_name} {id}')
        
        if command == 'destroy':
            self.onecmd(f'destroy {class_name} {id}')
        
        if command == 'update':
            pattern = r'\((.*?)\)'
            match = re.search(pattern, arg)
            if match:
                in_para = match.group(1).split(', ')
                id = in_para[0]
                att_name = in_para[1]
                value_name = in_para[2]
                self.onecmd(f'update {class_name} {id} {att_name} {value_name}')   

    def do_EOF(self, arg):
        '''Ctrl+Z to quit the program'''
        print()
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
