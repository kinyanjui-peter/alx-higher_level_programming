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

    """Update the class Base by adding the static method """
    @staticmethod
    def from_json_string(json_string):
        if json_string is None or len(json_string) == 0:
            return "[]"
        else:
            return json.loads(json_string)

    """ add the class method  returns an instance with 
        all attributes already set:"""
    def create(cls, **dictionary):
        """return an instance with all the attributes"""
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        else:
            dummy = cls(1)
        """dummy” instance to apply your real values"""
        dummy.update(**dictionary)
        return(dummy)

    @classmethod
    def load_from_file(cls):
        """
            Load List of Instance from JSON File
            """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                return [cls.create(**dictionary) for
                        dictionary in cls.from_json_string(f.read())]
        except FileNotFoundError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """
            save_to_file_csv
            """
        ld = []
        with open(cls.__name__ + ".csv", "w", encoding="utf-8") as f:
            if list_objs:
                for obj in list_objs:
                    if cls.__name__ == 'Rectangle':
                        ld.append([
                            obj.id, obj.width, obj.height, obj.x, obj.y])
                    if cls.__name__ == 'Square':
                        ld.append([obj.id, obj.size, obj.x, obj.y])
            writer = csv.writer(f)
            for row in ld:
                writer.writerow(row)

    @classmethod
    def load_from_file_csv(cls):
        """load_from_file_csv"""
        try:
            with open(cls.__name__ + ".csv", "r") as f:
                ld = []
                reader = csv.DictReader(f)
                for row in reader:
                    for key, val in row.items():
                        row[key] = int(val)
                ld.append(row)
                return [cls.create(**item) for item in ld]
        except FileNotFoundError:
            return []
