#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""
import cmd
import uuid
from datetime import datetime


class BaseModel(cmd.Cmd):
    """defines all common attributes/methods for other classes"""
    prompt = '(hbnb) '

    def __init__(self, *args, **kwargs):
        """class initialization"""
        if kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key != '__class__':
                    if key in ['created_at', 'updated_at']:
                        setattr(self, key, datetime.strptime(value, "%Y-%m-%dT%H:%M:%S.%f"))
                    else:
                        setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()

        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def __str__(self):
        """prints the class nicely"""
        result = []
        name = "[" + __class__.__name__ + "]"
        result.append(name)
        Id = '(' + self.id + ')'
        Dict = str(self.__dict__)
        result.append(Id)
        result.append(Dict)
        return " ".join(result)

    def save(self):
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()

    def to_dict(self):
        """returns a dictionary containing all
        keys/values of __dict__ of the instance"""
        Dict = self.__dict__
        Dict['__class__'] = __class__.__name__
        value = Dict.get('created_at')
        value = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
        Dict['created_at'] = value
        value = Dict.get('updated_at')
        value = value.strftime("%Y-%m-%dT%H:%M:%S.%f")
        Dict['updated_at'] = value
        return Dict

    def do_EOF(self, line):
        """enable EOF"""
        return True

    def postloop(self):
        """postloop action"""
        print


if __name__ == '__main__':
    BaseModel().cmdloop()
