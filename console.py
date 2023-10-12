#!/usr/bin/python3
"""
Contains the entry point of the command interpreter.
"""
import cmd


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
        raise NotImplementedError

    def do_show(self, arg):
        raise NotImplementedError

    def do_destroy(self, arg):
        raise NotImplementedError

    def do_all(self, arg):
        raise NotImplementedError

    def do_update(self, arg):
        raise NotImplementedError

    def do_EOF(self, arg):
        '''Ctrl+Z to quits the program'''
        return True


if __name__ == '__main__':
    HBNBCommand().cmdloop()
