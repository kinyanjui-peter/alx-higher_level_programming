#!/usr/bin/python3
"""import json"""
import json
"""
    class
    """


class Student:
    """
    class Student defination
    """
    def __init__(self, first_name, last_name, age):
        """
        initializes the attributes of class Student
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if attrs is None:
            """
            retrieves a dictionary representation of a Student instance
            """
            return {
                    "age " : self.age,
                    "last_name" : self.last_name,
                    "first_name " : self.first_name,
                    }
        else:
            dic = {}
            for attr in attrs:
                if hasattr(self, attr):
                    dic[attr] = getattr(self, attr)
            return dic

