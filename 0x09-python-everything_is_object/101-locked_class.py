#!/usr/bin/python3
"""Defines a lockedclass"""


class lockedClass:
    """Prevents te user from dynamically creating new instance
    except if the new instance attribute is called 'first_name'
    """

    __slots__ = ["first_name"]
