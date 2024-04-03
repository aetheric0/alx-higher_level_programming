#!/usr/bin/python3
from sys import stderr

def safe_function(fct, *args):
    try:
        x, y = args
        res = fct(x, y)
        return res
    except Exception as err:
        print("Exception:", err, file=stderr)
        return None
