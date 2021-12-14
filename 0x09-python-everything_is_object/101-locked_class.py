#!/usr/bin/python3
"""Defines a lockedclass"""


class lockedClass:
    """Prevents te user from dynamically creating new instance
    except if the new instance attributeis called first_name
    """
    __slots__ =["first_name"]
