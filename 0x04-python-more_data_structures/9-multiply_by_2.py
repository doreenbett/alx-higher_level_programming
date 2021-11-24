#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    '''Return a new dictionary with all values multiplied by 2.'''
    return ({c: a_dictionary[c] * 2 for c in a_dictionary})
