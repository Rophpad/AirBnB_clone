#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd
import re
from shlex import split
from models import storage
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.amenity import Amenity
from models.review import Review
from models.base_model import BaseModel


def parse(arg):
    """Parse user input before use it"""

class HBNBCommand(cmd.Cmd):
    """HBNBCommand class definition"""
    prompt = "(hbnb) "

    def postloop(self):
        """Postloop action"""
        pass

    def do_EOF(self, line):
        """Enable EOF"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel
        Save it to JSON file
        Print the id
        """
        try:
        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

if __name__ == "__main__":
    HBNBCommand().cmdloop()
