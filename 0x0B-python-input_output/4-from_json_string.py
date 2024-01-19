#!/usr/bin/python3
# 6-from_json_string.py
"""JSON_to_object function."""
import json


def from_json_string(my_str):
    """Return py_object for a JSON representaion"""
    return json.loads(my_str)
