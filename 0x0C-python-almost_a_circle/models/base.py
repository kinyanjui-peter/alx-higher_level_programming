#!/usr/bin/python3
"""import JSON"""
import json
"""creation of class base"""
class Base:
    """private class attribute"""
    __nb_objects = 0

    """init method defination"""
    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = self.__nb_objects

    """JSON data representation."""
    @staticmethod
    def to_json_string(list_dictionaries):
        if list_dictionaries is None:
            if len(list_dictionaries) == 0:
                return "[]"
        else:
            return json.dumps(list_dictionaries)

