#!/usr/bin/python3
"""FileStorage file"""

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """all"""
        return self.__objects

    def new(self, obj):
        """new"""

        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        """save"""

        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        """reload"""

        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded = json.load(file)

            classes = {
                'User': User,
                'BaseModel': BaseModel,
                'State': State,
                'City': City,
                'Amenity': Amenity,
                'Place': Place,
                'Review': Review
            }

            for key, obj_dict in loaded.items():
                class_name = obj_dict["__class__"]
                for model, clss in classes.items():
                    if class_name == model:
                        self.__objects[key] = clss(**obj_dict)

        except FileNotFoundError:
            pass
        except Exception as e:
            pass
