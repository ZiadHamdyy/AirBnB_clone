#!/usr/bin/python3

import json

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
        for key, obj in serialized:
            serialized[key] = obj.to_dect()

        with open(self.__file_path, 'w') as file:
            json.dump(serialized, file)
    def reload(self):
        try:
            with open(self.__file_path, 'r') as file:
                loaded = json.load(file)

            for key, obj_dict in loaded.item():
                class_name, obj_id = key.split('.')
                class_instance = globals()[class_name]
                obj = class_instance(obj_dict)
                self.__objects[key] = obj

        except FileNotFoundError:
            pass
