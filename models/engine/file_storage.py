#!/usr/bin/python3
"""serializes instances to a JSON file and deserializes
JSON file to instances"""
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """serializes instances to a JSON file and
    deserializes JSON file to instances"""

    __file_path = "file.json"
    __objects = {}
    all_class = {"BaseModel": BaseModel, "User": User, "Place": Place,
                 "City": City, "State": State, "Amenity": Amenity,
                 "Review": Review}

    def all(self):
        """returns the dictionary __objects"""
        return self.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file (path: __file_path)"""
        objDict = {}
        for key, obj in self.__objects.items():
            objDict[key] = obj.to_dict()
        with open(self.__file_path, 'w', encoding="UTF-8") as f:
            json.dump(objDict, f)

    def reload(self):
        """deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the
        file doesn’t exist"""
        try:
            with open(self.__file_path, 'r', encoding='UTF-8') as f:
                data = json.load(f)
                for key, value in data.items():
                    obj = self.all_class[value['__class__']](**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
