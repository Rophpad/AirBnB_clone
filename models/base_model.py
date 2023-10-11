#!/usr/bin/python3
"""defines all common attributes/methods for other classes"""
import uuid
from datetime import datetime
#from models.__init__ import storage


class BaseModel:
    """defines all common attributes/methods for other classes"""

    def __init__(self, *args, **kwargs):
        from models.__init__ import storage
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
            self.updated_at = datetime.now()
            storage.new(self)

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
        from models.__init__ import storage
        """updates the public instance attribute
        updated_at with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

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
