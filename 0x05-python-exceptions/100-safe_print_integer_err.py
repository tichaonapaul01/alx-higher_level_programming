#!/usr/bin/python3
import sys

def safe_print_integer_err(value):
    try:
        value_as_int = int(value)
        print(value_as_int)
        return True
    except ValueError as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
    except Exception as e:
        print("Exception: {}".format(e), file=sys.stderr)
        return False
