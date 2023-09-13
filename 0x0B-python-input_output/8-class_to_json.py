#!/usr/bin/python3

"""
    Class to JSON
    """


def class_to_json(obj):
    """
    returns the dictionary description with
    simple data structure
    (list, dictionary, string, integer and boolean)
    for JSON serialization of an object
    args:
        @obj: is an instance of a Class
        nb/:All attributes of the obj Class are serializable:
    """
    return obj.__dict__
