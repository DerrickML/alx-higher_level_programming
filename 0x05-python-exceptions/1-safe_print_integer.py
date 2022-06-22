#!/usr/bin/python3

def safe_print_integer(value):
    """
    prints an integer
        Returns True if value has been correctly printed
        Otherwise False
    """
    try:
        print("{:d}".format(value))
        return True
    except (ValueError, TypeError):
        return False
