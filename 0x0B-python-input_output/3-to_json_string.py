#!/usr/bin/python3
import json
"""function that returns
the JSON representation of an object (string)
"""
def to_json_string(my_obj):
    """
        args:
            @my_obj: object to be converted to JSON
            returns: JSON string
            """

    convertedto_json = json.dump(my_obj)
    return convertedto_json
