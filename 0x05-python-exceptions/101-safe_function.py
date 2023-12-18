#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        result = fct(*args)
        return (result)
    except Exception as a:
        print("Exception: {}".format(a), file=sys.stderr)
        return (None)
