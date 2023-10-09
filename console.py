#!/usr/bin/python3
"""
Contains the entry point of the command interpreter.
"""


class HBNBCommand(cmd.Cmd):
    """The console command interpreter."""
    prompt = "(hbnb)"

    def emptyline(self):
        raise NotImplementedError

    def do_quit(self, arg):
        raise NotImplementedError

    def do_help(self, arg):
        raise NotImplementedError

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


if __name__ == '__main__':
    HBNBCommand().cmdloop()
