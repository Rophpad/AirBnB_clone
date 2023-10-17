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
    curlyBraces = re.search(r"\{(.*?)\}", arg)
    brackets = re.search(r"\[(.*?)\]", arg)
    if curlyBraces is None:
        if brackets is None:
            return [i.strip(",") for i in split(arg)]
        else:
            lexer = split(arg[:brackets.span()[0]])
            rtl = [i.strip() for i in lexer]
            rtl.append(brackets.group())
            return rtl
    else:
        lexer = split(arg[:curly_braces.span()[0]])
        rtl = [i.strip() for i in lexer]
        rtl.append(curly_braces.group())
        return rtl


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class definition"""
    prompt = "(hbnb) "
    __classes = {"BaseModel", "User", "State", "City",
                 "Place", "Amenity", "Review"}

    def emptyline(self):
        """Postloop action"""
        pass

    def do_EOF(self, line):
        """Enable EOF"""
        print("")
        return True

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_create(self, arg):
        """Creates a new instance of BaseModel
        Save it to JSON file
        Print the id
        """
        args = parse(arg)
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            print(eval(args[0])().id)
            storage.save()

    def do_show(self, arg):
        """Prints the string representation of an instance
        based on the class name and id
        """
        args = parse(arg)
        Dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id missing **")
        elif "{}.{}".format(args[0], args[1]) not in Dict:
            print("** no instance found **")
        else:
            print(Dict["{}.{}".format(args[0], args[1])])

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = parse(arg)
        Dict = storage.all()
        if len(args) == 0:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) == 1:
            print("** instance id doesn't exist **")
        elif "{}.{}".format(args[0], args[1]) not in Dict:
            print("** no instance found **")
        else:
            del Dict["{}.{}".format(args[0], args[1])]
            storage.save()

    def do_all(self, arg):
        """Prints all string repr of all instances"""
        args = parse(arg)
        if len(args) > 0 and args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            all_obj = []
            for obj in storage.all().values():
                if len(args) > 0 and args[0] == obj.__class__.__name__:
                    all_obj.append(obj.__str__())
                elif len(args) == 0:
                    all_obj.append(obj.__str__())
                print(all_obj)

    def do_update(self, arg):
        """Update instance"""
        args = parse(arg)
        Dicts = storage.all()

        if len(args) == 0:
            print("** class name missing **")
            return False
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        elif len(args) == 1:
            print("** instance id missing **")
            return False
        elif "{}.{}".format(args[0], args[1]) not in Dicts:
            print("** no instance found **")
            return False
        elif len(args) == 2:
            print("** attribute name missing **")
            return False
        elif len(args) == 3:
            try:
                type(eval(args[2])) != dict
            except NameError:
                print("** value missing **")
                return False
        elif len(args) == 4:
            obj = Dicts["{}.{}".format(args[0], args[1])]
            if args[2] in obj.__class__.__dict__.keys():
                val_type = type(obj.__class__.__dict__[args[2]])
                obj.__dict__[args[2]] = val_type(args[3])
            else:
                obj.__dict__[args[2]] = args[3]
        elif type(eval(args[2])) == dict:
            obj = Dicts["{}.{}".format(args[0], args[1])]
            for k, v in eval(args[2]).items():
                kkeys = k in obj.__class__.__dict__.keys()
                type_in = type(obj.__class__.__dict__[k]) in {str, int, float}
                if (kkeys and type_in):
                    val_type = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = val_type(v)
                else:
                    obj.__dict__[k] = v
        storage.save()

    def do_count(self, arg):
        """Retrieve the number of instances of a class"""
        args = parse(arg)
        count = 0
        for obj in storage.all().values():
            if argl[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def default(self, arg):
        """handle special case command"""
        show = r'show\("([^"]*)"\)'
        destroy = r'destroy\("([^"]*)"\)'
        update = r'update\("([^"]*)", ?"([^"]*)", ?"([^"]*)"\)'
        update_v2 = r'update\("([^"]*)", ?(\{[^}]+\})'
        cmd_arg = ['all()', 'count()', show, destroy, update, update_v2]
        if arg:
            _class, method = arg.split('.')
            if _class in HBNBCommand.__classes:
                if method == cmd_arg[0]:
                    for k, v in storage.all().items():
                        key, _ = k.split('.')
                        if key == _class:
                            print(v)
                elif method == cmd_arg[1]:
                    count = 0
                    for k in storage.all():
                        key, _ = k.split('.')
                        if key == _class:
                            count += 1
                    print(count)
                elif re.search(cmd_arg[2], method) is not None:
                    Id = (re.search(cmd_arg[2], method)).group(1)
                    arg = '{} {}'.format(_class, Id)
                    self.do_show(arg)
                elif re.search(cmd_arg[3], method) is not None:
                    Id = (re.search(cmd_arg[3], method)).group(1)
                    arg = '{} {}'.format(_class, Id)
                    self.do_destroy(arg)
                elif re.search(cmd_arg[4], method) is not None:
                    Id = (re.search(cmd_arg[4], method)).group(1)
                    key = (re.search(cmd_arg[4], method)).group(2)
                    value = (re.search(cmd_arg[4], method)).group(3)
                    arg = '{} {} {} {}'.format(_class, Id, key, value)
                    self.do_update(arg)
                elif re.search(cmd_arg[5], method) is not None:
                    Id = (re.search(cmd_arg[5], method)).group(1)
                    Dict = (re.search(cmd_arg[5], method)).group(2)
                    Dict = eval(Dict)
                    for key, value in Dict.items():
                        arg = '{} {} {} {}'.format(_class, Id, key, value)
                        self.do_update(arg)


if __name__ == "__main__":
    HBNBCommand().cmdloop()
