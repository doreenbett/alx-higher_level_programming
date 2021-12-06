#!/usr/bin/python3
def safe_print_division(a, b):
    '''Divides 2 integers and prints result
    Args: a, b
    Returns: value of division, otherwise none
    '''
    try:
        res = a / b
    except (TypeError, ZeroDivisionError):
        res = None
    finally:
        print("Inside result: {}".format(res))
    return (res)
