#!/usr/bin/python3
"""Entry point of the command interpreter"""
import cmd


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

if __name__ == "__main__":
    HBNBCommand().cmdloop()
