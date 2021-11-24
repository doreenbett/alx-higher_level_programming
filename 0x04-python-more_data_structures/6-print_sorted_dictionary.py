#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    '''Print a dictionary by ordered keys.'''
    [print("{}: {}".format(c, a_dictionary[c])) for c in sorted(a_dictionary)]
