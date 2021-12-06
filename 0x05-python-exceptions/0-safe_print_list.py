#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''Prints x elements of a list
    Args: my_list=[] contains any type and x represents
         the number of elements printed
    Returns: real number of elements printed
    '''
    ret = 0
    for i in range(x):
        try:
            print("{:d}".format(my_list[i]), end="")
            ret += 1
        except IndexError:
            break
    print("")
    return (ret)
