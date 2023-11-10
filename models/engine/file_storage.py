#!/usr/bin/python3

import json
from models.base_model import BaseModel

class FileStorage:
    """FileStorage class"""

    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new( self, obj):
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        serialized = {}
        for key, obj in self.__objects.items():
            serialized[key] = obj.to_dict()

        with open(self.__file_path, 'w', encoding='utf-8') as file:
            json.dump(serialized, file)

    def reload(self):
        try:
            with open(self.__file_path, 'r', encoding='utf-8') as file:
                loaded = json.load(file)
            
            for key, obj_dict in loaded.items():
                class_name, obj_id = key.split('.')
                class_instance = globals()[class_name]
                obj = class_instance(**obj_dict)
                self.__objects[key] = obj
        except FileNotFoundError:
            pass
