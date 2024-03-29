#!/usr/bin/python3
"""
json file
"""
import json
"""
function that returns an object (Python data structure)
represented by a JSON string
"""


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string"""
    return json.loads(my_str)
