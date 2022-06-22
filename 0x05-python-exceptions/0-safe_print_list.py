#!/usr/bin/python3


def safe_print_list(my_list=[], x=0):
    """
    print x elements of a list, which must only be integer
    returns the number of elements printed
    """
    num = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            num += 1
        except (ValueError, TypeError):
            pass
        except IndexError:
            break
    print()
    return num
