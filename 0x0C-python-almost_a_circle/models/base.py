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

    """writes the JSON string representation of list_objs to a file:"""
    @classmethod
    def save_to_file(cls, list_objs):
        """writes the JSON string representation of list_objs to a file"""
        if list_objs is None:
            list_objs = []
        filename = cls.__name__ + ".json"
        obj_dict = [obj.to_dictionary() for obj in list_objs]
        json_data = cls.to_json_string(obj_dict)
        with open(filename, 'w',) as json_file:
            json_file.write(json_data)
