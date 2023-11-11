#!/usr/bin/python3
"""FileStorage file"""

import json
from models.base_model import BaseModel
from models.user import User
<<<<<<< HEAD
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
=======
from models.place import Place
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.review import Review

>>>>>>> f03d2ff600668bf0957e70f174b06e2734645cd4

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

            models = {
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
                class_instance = models.get(class_name)

                if class_instance:
                    obj = class_instance(**obj_dict)
                    self.__objects[key] = obj

        except FileNotFoundError:
            pass
