#!/usr/bin/python3
"""Defines an inherited list class Mylist."""


Class Mylist(list):
    """Implements sorted printing for the  built-in list class"""

    def print_sorted(self):
        """Print a list in sorted ascendig order"""
        print(sorted(self))
