#!/usr/bin/python3
"""JSON file write"""
import json


def save_to_json_file(my_obj, filename):
    """Writes to file the JSON rep of py_obj"""
    with open(filename, "w") as f:
        json.dump(my_obj, f)
